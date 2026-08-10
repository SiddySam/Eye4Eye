# Markdown Cheat Sheet

## Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

---

## Text Formatting

```markdown
**Bold**

*Italic*

***Bold and italic***

~~Strikethrough~~

`Inline code`
```

---

## Paragraphs

Just write normally.

```markdown
This is a paragraph.

This is a new paragraph.
```

---

## Line Break

Two spaces at the end of a line:

```markdown
Line one  
Line two
```

Or use an HTML break:

```markdown
Line one<br>
Line two
```

---

## Unordered Lists

```markdown
- Item
- Item
- Item
```

Result:

* Item
* Item
* Item

### Nested Lists

```markdown
- Main item
  - Sub item
  - Sub item
    - Sub-sub item
- Main item
```

---

## Ordered Lists

```markdown
1. First
2. Second
3. Third
```

Result:

1. First
2. Second
3. Third

---

## Checkboxes / Task Lists

```markdown
- [ ] Not completed
- [x] Completed
```

Result:

* [ ] Not completed
* [x] Completed

---

## Links

```markdown
[Google](https://www.google.com)
```

Result:

[Google](https://www.google.com)

### Link with Title

```markdown
[Google](https://www.google.com "Google Homepage")
```

---

## Images

```markdown
![Image description](image.png)
```

Example:

```markdown
![Screenshot](images/screenshot.png)
```

---

## Code

### Inline Code

```markdown
Use `python3` to run Python.
```

### Code Block

````markdown
```python
print("Hello world!")
```
````

### Bash

````markdown
```bash
sudo apt update
python3 scraper.py
```
````

### Plain Text

````markdown
```text
Project/
├── README.md
├── src/
└── tests/
```
````

---

## Block Quotes

```markdown
> This is a quote.
```

Result:

> This is a quote.

### Multiple Lines

```markdown
> First line
> Second line
> Third line
```

---

## Horizontal Line

```markdown
---
```

or:

```markdown
***
```

---

## Tables

```markdown
| Name | Type | Status |
|------|------|--------|
| Python | Language | Done |
| Git | Tool | Done |
| Database | Backend | TODO |
```

Result:

| Name     | Type     | Status |
| -------- | -------- | ------ |
| Python   | Language | Done   |
| Git      | Tool     | Done   |
| Database | Backend  | TODO   |

### Table Alignment

```markdown
| Left | Centre | Right |
|:-----|:------:|------:|
| A    | B      | C     |
| D    | E      | F     |
```

---

## Escaping Markdown

If you need to display a Markdown character rather than have Markdown interpret it:

```markdown
\*This won't be italic\*
```

Common characters to escape:

```text
\* \_ \# \- \+ \. \! \[ \] \( \) \` \>
```

---

## Nested Formatting

You can combine formatting:

```markdown
**This is bold with `code` inside it.**

*This is italic with **bold** inside it.*
```

---

## Collapsible Sections

GitHub supports HTML inside Markdown:

````html
<details>
<summary>Click to expand</summary>

Hidden content goes here.

```bash
echo "Hello"
````

</details>
```

---

## Badges

GitHub READMEs commonly use badges:

```markdown
![GitHub license](https://img.shields.io/github/license/USERNAME/REPOSITORY)
```

Example:

```markdown
![Python](https://img.shields.io/badge/python-3.x-blue)
```

---

## Emoji

GitHub supports emoji shortcodes:

```markdown
:rocket:
:computer:
:white_check_mark:
:warning:
:x:
```

For example:

```markdown
🚀 Project started!
```

---

## HTML

GitHub Markdown allows some HTML:

```html
<p align="center">
  <img src="logo.png" width="200">
</p>
```

You can also use:

```html
<br>
<hr>
```

---

## Comments

You can add comments that won't appear on the rendered page:

```html
<!-- This is a comment -->
```

Useful for leaving notes in a README.

---

# Useful README Structure

A typical project README might look like:

````markdown
# Project Name

Short description of the project.

## Features

- Feature one
- Feature two
- Feature three

## Requirements

- Python 3
- Ubuntu Linux
- BeautifulSoup

## Installation

```bash
git clone https://github.com/username/project.git
cd project
pip install -r requirements.txt
````

## Usage

```bash
python3 main.py
```

## Project Structure

```text
project/
├── README.md
├── main.py
├── requirements.txt
└── src/
```

## TODO

* [x] Initial setup
* [x] Git repository
* [ ] Implement feature
* [ ] Write tests

## Known Issues

* None currently.

## License

MIT

````

---

# The Ones You'll Use Most

If you're just starting with Markdown, memorise these:

```markdown
# Heading

**bold**

*italic*

- bullet

1. numbered

[link](https://example.com)

![image](image.png)

`code`

```python
code block
````

> quote

---

* [ ] TODO
* [x] Done

```

Those cover **the vast majority of README writing** you'll need.
```
