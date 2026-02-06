# Python Dictionary (Tkinter)

A simple desktop **dictionary application** built with **Tkinter** that fetches word meanings using a free online dictionary API.  
It provides a clean interface to search for English words and view their definitions grouped by part of speech.

---

## Features

- Search meanings of English words instantly  
- Displays **multiple definitions** organized by part of speech  
- Clean dark-themed graphical interface  
- Scrollable result area for long definitions  
- Error handling for:
  - Empty input  
  - Word not found  
  - No internet connection  
  - Server errors  

---

## Requirements

Make sure Python is installed, then install the required library:

```bash
pip install requests
```

**Tkinter** usually comes pre-installed with Python.

---

## How to Run

1. Download the Python file and the required `icon.png`.  
2. Open a terminal in the project folder.  
3. Run:

```bash
python filename.py
```

The application window will open.

---

## How to Use

1. Enter an **English word** in the input field.  
2. Press **Enter** or click the **Search** button.  
3. Meanings will appear in the results section below.  

---

## Notes

- Internet connection is required to fetch definitions.  
- Uses the free public API from **dictionaryapi.dev**.  
- Only English words are supported.  

---
