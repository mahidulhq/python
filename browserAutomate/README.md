# Automate WebBrowser

Automatically opens specific multiple websites in browser(default/manual) tabs.

## Python Libraries Used

- `webbrowser` - Cross-platform browser control

## Features

- Opens multiple URLs in **new tabs**
- **Default browser** mode (recommended)
- **Custom browser** support (Windows/Linux)
- Progress logging to console

## Default URLs Opened

- `https://www.github.com/mahidulhq`
- `https://mahidulhq.github.io/`

## Usage

```bash
python web_opener.py
```

**Output:**
```
opening : https://www.github.com/mahidulhq
opening : https://mahidulhq.github.io/
```

## Browser Configuration

**Default (recommended):**
```python
wb.open_new_tab(url)  # Uses system default browser
```

**Custom Chrome (Linux snap):**
```python
chrome_path = '/snap/bin/chromium %s'
wb.get(chrome_path).open(url)
```

## Platform Notes

| OS | Default Behavior | Custom Path Example |
|---|------------------|-------------------|
| **Linux** | Default browser | `/snap/bin/chromium %s` |
| **Windows** | Default browser | `C:\Program Files\Google\Chrome\Application\chrome.exe %s` |
| **macOS** | Default browser | `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome %s` |

## Code Flow

```
Define URLs → Loop each URL → Print → Open new tab → Next
```

## Limitations

- Fixed URL list (hardcoded)
- Sequential opening (not parallel)
- Custom browser path needs manual config
- No error handling
- Single execution
