# File Sorter (Python Tkinter)

A simple desktop **file organization tool** built with **Tkinter** that helps you automatically sort files inside a selected directory based on their file extensions.

---

## Features

- Choose any folder from your system
- Automatically sorts files into categorized folders such as:
  - Images  
  - Videos  
  - Music  
  - Documents  
  - Python files  
  - Executables  
- Creates new folders if they don’t already exist
- Handles unknown file extensions by creating separate folders
- Simple and minimal dark-theme GUI
- Error handling with message popups

---

## Requirements

No external libraries are required.

This project only uses:

- **Python standard library**
  - `tkinter`
  - `os`

Tkinter usually comes pre-installed with Python.

---

## How to Run

1. Download the Python file.
2. Open terminal or command prompt in the project folder.
3. Run:

```bash
python filename.py
```

The **File Sorter window** will open.

---

## How to Use

1. Click **"Choose Directory"**.
2. Select the folder you want to organize.
3. Click **"Sort Files"**.
4. Files will automatically move into categorized folders inside the selected directory.

---

## Sorting Rules

| Extension | Folder Name |
|-----------|-------------|
| `.jpg`, `.jpeg`, `.png` | Images |
| `.mp4` | Videos |
| `.mp3` | Music |
| `.py` | Python |
| `.exe` | Executables |
| `.docx` | Documents |
| `.pptx` | Presentation |
| `.txt` | Text Documents |
| Others | `<extension> Files` |

Shortcuts (`.lnk`) and the script file itself are ignored.

---

## Notes

- Files are **moved**, not copied.
- Make sure no important program is running from the selected folder.
- Works on **Windows, Linux, and macOS** (with Python installed).

---
