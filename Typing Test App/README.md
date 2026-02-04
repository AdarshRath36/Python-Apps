# Python Typing Speed Test

This is a desktop typing speed test application built using Python and Tkinter.  
It measures a user’s typing speed in words per minute (WPM) and calculates typing accuracy based on a reference sentence.

The app is designed to practice GUI development, event handling, file handling, and basic performance calculations in Python.

---

## Features

- Random sentence generation for each test
- Real-time timer
- Calculates:
  - Words Per Minute (WPM)
  - Typing accuracy (%)
- High score system (name, WPM, accuracy)
- Save and view high scores
- User profile support
- Keyboard-based interaction
- Clean and readable interface

---

## Technologies Used

- Python
- Tkinter (GUI)
- OS module (file handling)
- Random module

---

## Project Structure

typing-test/
├─ app.py
├─ README.md
└─ highscore.txt
> The `highscore.txt` file is created automatically if it does not exist.

---

## How to Run the Application

### 1. Requirements
- Python 3.x installed on the system
- Windows OS (uses Windows user directory for high score storage)

### 2. Run the App
Open a terminal in the project folder and run:
python app.py
---

## How the Test Works

1. A random sentence is displayed
2. Click **Start** or begin typing to start the timer
3. Type the sentence as accurately as possible
4. Press **Enter** to finish the test
5. WPM and accuracy are calculated and displayed

---

## Keyboard Shortcuts

| Action | Shortcut |
|------|---------|
| Start timer | Start typing |
| Finish test | Enter |
| Save high score | Ctrl + S |

---

## High Score System

- Stores:
  - Username
  - Best WPM
  - Best accuracy
- High scores are saved locally in a text file
- New scores overwrite previous ones only if both WPM and accuracy are higher

---

## Notes

- WPM is calculated using total words typed and time taken
- Accuracy is calculated by comparing character-by-character input
- Designed mainly for learning and personal use
- Best tested on Windows systems

---

## Possible Improvements

- Add multiple difficulty levels
- Add countdown-based test mode
- Improve accuracy calculation logic
- Support cross-platform file paths

---
