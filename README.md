# Claude Chat History Viewer

- **Course:** CMU 17-316
- **Purpose:** A better way to view and submit Claude Code chat history in markdown format

## Overview

This repository contains my Claude Code chat history for CMU 17-316, along with a custom web-based markdown viewer. As the chat history grows longer, viewing it in a standard markdown viewer becomes increasingly difficult. This tool provides a better reading experience with syntax highlighting, table of contents, and smooth navigation.

## What's Inside

- **`viewer.html`** - Modern static web page for visualizing markdown files with:
  -  **Dark/Light mode toggle** - Switch between themes with saved preference

- **`P4ClaudeChatHistory.md`** - Complete chat history from Claude Code sessions of P4 by Watson

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
   - Click the "Choose File" button
   - Select the chat history you want to view
   - Enjoy a beautifully formatted, easy-to-navigate view of the chat history!

4. **Customize your experience** (Optional)
   - Click the theme toggle button (🌙/☀️) in the top-right corner to switch between dark and light modes
   - Your preference will be saved for future visits

## Why This Approach?

Claude Code chat histories can become quite lengthy, and traditional markdown viewers don't handle long documents well. This tool was created to:

- Provide a better reading experience for graders/reviewers
- Enable quick navigation through long conversations via table of contents
- Ensure proper syntax highlighting for code snippets
- Make the submission more professional and accessible

## Technical Details

The viewer uses:
- [Marked.js](https://marked.js.org/) for markdown parsing
- [Highlight.js](https://highlightjs.org/) for syntax highlighting with dual themes (Atom One Dark/Light)
- CSS Variables for dynamic theming
- LocalStorage API for theme persistence
- Modern CSS (gradients, glassmorphism, animations)
- Vanilla JavaScript (no frameworks needed)

---

### **Note:** This is the best solution I've found for submitting Claude Code chat history while maintaining readability and usability. Feel free to use this approach for your own submissions!
