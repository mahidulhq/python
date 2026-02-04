# Simple Screenshot App

A minimal Python script that captures and saves screenshots with timestamps to a dedicated folder.

## Features

- Automatic timestamp-based filename generation
- Saves screenshots to `/screenshotData` folder
- 5-second delay before capture
- Automatically displays the captured image


## Project Structure

```
project01/
├── screenshot.py          # Main script
├── venv/                  # Virtual environment
└── screenshotData/        # Screenshot storage (auto-created)
```


## Requirements

- Python 3.x
- `pyautogui` (`pip install pyautogui`)


## Setup

1. Activate virtual environment: `source venv/bin/activate` (Linux/Mac)
2. Install dependencies: `pip install pyautogui`

## Usage

```bash
python screenshot.py
```

- Script starts 5-second countdown
- Captures full screen
- Saves as `/screenshotData/{timestamp}.png`
- Opens image automatically


## How It Works

1. Generates unique filename using current timestamp (milliseconds)
2. Waits 5 seconds for user to position screen
3. Uses `pyautogui.screenshot()` to capture entire screen
4. Saves to `screenshotData/` folder
5. Displays image using default viewer

## Notes [RECOMMENDED]

- Hardcoded path: `/home/panda/Documents/python_learning/python/screenshotAPP_CLI/screenshotData/`
- Modify path in script for different systems
- Ensure `screenshotData` folder exists or has write permissions

***

for further development: [pyautogui doc](https://pyautogui.readthedocs.io/en/latest/install.html)  
