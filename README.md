# Static Site Generator 

A simple static site generator built in Python.

It converts Markdown files from `content/` into HTML pages, copies static assets (CSS/images) from `static/`, and outputs a complete site to `docs/` for GitHub Pages hosting.

## Features

- Markdown → HTML conversion
- Supports block-level Markdown:
  - headings
  - paragraphs
  - code blocks
  - quotes
  - unordered lists
  - ordered lists
- Supports inline Markdown:
  - bold (`**text**`)
  - italic (`_text_`)
  - code (`` `text` ``)
  - links (`[text](url)`)
  - images (`![alt](url)`)
- Copies static assets recursively (`static/` → `docs/`)
- Generates pages recursively for nested content directories
- Configurable base path for GitHub Pages (`/REPO_NAME/`)

## Project Structure

- `content/` — Markdown source files (your pages/posts)
- `static/` — Static assets (CSS, images, etc.)
- `template.html` — HTML template used for all pages
- `src/` — Generator source code + unit tests
- `docs/` — Generated site output (committed for GitHub Pages)

## Requirements

- Python 3 (tested with Python 3.12+)
- No external dependencies (standard library only)

## Run locally

Generate the site into `docs/` using the default base path `/`:

```bash
./main.sh
