# Simple Image OCR Text Extractor

Extracts text from images using Tesseract OCR.

## Python Libraries Used

- `pytesseract` - Python wrapper for Tesseract OCR engine
- `PIL` (Pillow) - Image processing
- `os` - File operations

## Prerequisites

1. **Install Tesseract OCR**:
   - Windows: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Ubuntu: `sudo apt install tesseract-ocr`
   - macOS: `brew install tesseract`

2. **Python packages**:
   ```bash
   pip install pytesseract pillow
   ```

## Features

- Converts single JPG image to plain text
- Prints extracted text to console
- Uses default Tesseract language (English)

## Usage

1. Place `imagee.jpg` in project directory
2. Run script:
   ```bash
   python ocr_reader.py
   ```
3. Extracted text prints to terminal

## Code Flow

```
Image.open("imagee.jpg") → pytesseract.image_to_string() → print()
```

## Example

```python
# Input: imagee.jpg containing "Hello World"
# Output: Hello World
```

## Limitations

- Fixed filename (`imagee.jpg`) or you can change the file name on .py file  
- No error handling
- English-only (default)
- Console output only
- Single image processing

***