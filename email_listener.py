import ollama
import imaplib
import email
import os
import logging
import sys

log_file = open("email_listener.log", "a")

class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, data):
        for file in self.files:
            file.write(data)
            file.flush()

    def flush(self):
        for file in self.files:
            file.flush()

sys.stdout = Tee(sys.stdout, log_file)

# Your existing program goes here

EMAIL = os.getenv("e4eEmail")
PASSWORD = os.getenv("e4ePass")

mail = imaplib.IMAP4_SSL("imap.gmail.com")

mail.login(EMAIL, PASSWORD)

mail.select("INBOX")


def move_email(uid, destination):
    # Copy the email to the destination mailbox
    status, data = mail.uid(
        "COPY",
        uid,
        destination
    )

    if status != "OK":
        print("Failed to copy email to:", destination)
        return False

    # Only delete the original if the copy succeeded
    status, data = mail.uid(
        "STORE",
        uid,
        "+FLAGS",
        r"(\Deleted)"
    )

    if status != "OK":
        print("Email copied, but failed to mark original as deleted.")
        return False

    # Permanently remove the original from INBOX
    mail.expunge()

    print("Email moved to:", destination)

    return True


def parse_email(raw_email, uid):
    msg = email.message_from_bytes(raw_email)

    body = ""

    if msg.is_multipart():

        for part in msg.walk():

            if part.get_content_type() == "text/plain":

                payload = part.get_payload(decode=True)

                if payload:
                    body = payload.decode(errors="replace")

                break

    else:

        payload = msg.get_payload(decode=True)

        if payload:
            body = payload.decode(errors="replace")

    return {
        "uid": uid,
        "from": msg["From"],
        "subject": msg["Subject"],
        "body": body
    }



def ask_ollama(email_data):

    prompt = f"""
You are an email assistant for a mechanics shop.

Analyse the following email.

From: {email_data["from"]}
Subject: {email_data["subject"]}

Body:
{email_data["body"]}

Answer with a single word only, answer 'Yes' if this email feels like its not related to this business or could be a scam, or answer 'No' if this email seems normal for the business .
"""

    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]




# Find the newest UID currently in the mailbox
status, data = mail.uid("search", None, "ALL")

uids = data[0].split()

if uids:
    last_uid = int(uids[-1])
else:
    last_uid = 0


print("Connected.")
print("Starting from UID:", last_uid)
print("Waiting for new emails...")


while True:

    new_email = False

    # Wait for Gmail
    with mail.idle(duration=300) as idler:

        for response in idler:

            print("SERVER RESPONSE:", response)

            if response[0] == "EXISTS":

                new_email = True
                break


    # IDLE has now ended

    if new_email:

        # Find all UIDs we haven't processed
        status, data = mail.uid(
            "search",
            None,
            f"UID {last_uid + 1}:*"
        )

        new_uids = data[0].split()

        for uid in new_uids:

            uid_number = int(uid)

        # Fetch email
        status, data = mail.uid(
            "fetch",
            uid,
            "(RFC822)"
        )

        raw_email = None

        for item in data:
            if isinstance(item, tuple) and isinstance(item[1], bytes):
                raw_email = item[1]
                break

        if raw_email is None:
            print("Could not retrieve email data.")
            continue

        # Convert raw email into our dictionary
        email_data = parse_email(
            raw_email,
            uid_number
        )

        print("\n==============================")
        print("NEW EMAIL")
        print("==============================")

        print("UID:", email_data["uid"])
        print("From:", email_data["from"])
        print("Subject:", email_data["subject"])
        print("Body:")
        print(email_data["body"])

        analysis = ask_ollama(email_data)

        analysis = analysis.strip().lower()

        print("\n--- OLLAMA ---")
        print(analysis)

        if analysis == "yes":

            print("Ollama wants to move this email somewhere else")

            success = move_email(
                uid,
                "filtered"
            )

            if success:
                print("Email successfully moved.")

        elif analysis == "no":

            print("Ollama thinks this email is ok")

    else:

        print("Ollama has something else to say:", analysis)

    print("==============================")
    last_uid = uid_number
    print("\nWaiting for new emails...")
