# Claude Chat History Viewer

> **Course:** CMU 17-316
> **Purpose:** A better way to view and submit Claude Code chat history in markdown format

## Overview

This repository contains my Claude Code chat history for CMU 17-316, along with a custom web-based markdown viewer. As the chat history grows longer, viewing it in a standard markdown viewer becomes increasingly difficult. This tool provides a better reading experience with syntax highlighting, table of contents, and smooth navigation.

## What's Inside

- **`viewer.html`** - Static web page for visualizing markdown files with:
  - GitHub-style formatting
  - Automatic table of contents generation
  - Syntax highlighting for code blocks
  - Responsive design
  - Smooth scrolling navigation
  - "Back to top" button

- **`P4ClaudeChatHistory.md`** - Complete chat history from Claude Code sessions

- **`extract_chat_history.py`** - Python script used to extract chat history from Claude Code

## How to Use

### Quick Start

1. **Clone this repository**
   ```bash
   git clone https://github.com/chaowatson/claude_extract.git
   cd claude_extract
   ```

2. **Open the viewer**
   ```bash
   open viewer.html
   ```
   Or simply double-click `viewer.html` in your file browser

3. **Load the chat history**
   - Click the "Choose Markdown File" button
   - Select `P4ClaudeChatHistory.md`
   - Enjoy a beautifully formatted, easy-to-navigate view of the chat history!

### Features

- **No server required** - Works entirely in your browser
- **No CORS issues** - Uses browser's FileReader API
- **Fast rendering** - Even with large markdown files

## Why This Approach?

Claude Code chat histories can become quite lengthy, and traditional markdown viewers don't handle long documents well. This tool was created to:

- Provide a better reading experience for graders/reviewers
- Enable quick navigation through long conversations via table of contents
- Ensure proper syntax highlighting for code snippets
- Make the submission more professional and accessible

## Technical Details

The viewer uses:
- [Marked.js](https://marked.js.org/) for markdown parsing
- [Highlight.js](https://highlightjs.org/) for syntax highlighting
- Pure CSS for GitHub-style formatting
- Vanilla JavaScript (no frameworks needed)

---

**Note:** This is the best solution I've found for submitting Claude Code chat history while maintaining readability and usability. Feel free to use this approach for your own submissions!
