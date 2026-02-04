# Simple Screenshot App with GUI

A minimal Python script that captures and saves screenshots with instant to a dedicated folder.

## Features

- Two buttons -->  Capture and QUIT
- Automatic timestamp-based filename generation
- Saves screenshots to `/screenshotData` folder 
- Instant capture
- Automatically displays the captured image


## Project Structure

```
project01/
├── screenshot.py          # Main script
├── venv/                  # Virtual environment
└── screenshotData/        # Screenshot storage (auto-created)
```


## Requirements

- Python
- `pyautogui` (`pip install pyautogui`)


## Setup

1. Activate virtual environment: `source venv/bin/activate` (Linux/Mac)
2. Install dependencies: `pip install pyautogui`

## Usage

```bash
python screenshot.py
```


## How It Works

1. Generates unique filename using current timestamp (milliseconds)
2. Capture full screen instantly
3. Uses `pyautogui.screenshot()` to capture entire screen
4. Saves to `screenshotData/` folder
5. Displays image using default viewer

## Notes [RECOMMENDED]

- Hardcoded path: `/home/panda/Documents/python_learning/python/project01/screenshotData/`
- Modify path in script for different systems
- Ensure `screenshotData` folder exists or has write permissions

***

For future development:   
- [pyautogui doc](https://pyautogui.readthedocs.io/en/latest/install.html)  
- [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)