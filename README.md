# Threads Native App for Windows

A native Windows application that displays Threads (https://www.threads.net) in a dedicated window without browser UI.

## Features

- Native window without browser toolbar or navigation buttons
- Remembers window size and position between launches
- Uses Microsoft Edge WebView2 for modern web compatibility
- Configuration saved in `~/.threads-app/window-config.json`

## Prerequisites

- Windows 10 or Windows 11
- Python 3.7 or higher
- WebView2 runtime (usually pre-installed on modern Windows)

## Quick Start

### Option 1: Using PowerShell (Recommended)

1. Open PowerShell as regular user (no admin required)
2. Navigate to this directory
3. Run: `.\build-threads-app.ps1`

### Option 2: Using Command Prompt

1. Open Command Prompt
2. Navigate to this directory
3. Run: `build-threads-app.bat`

### Option 3: Manual Build

1. Install dependencies:
   ```
   pip install pywebview pyinstaller
   ```

2. Build the executable:
   ```
   python -m PyInstaller --onefile --windowed --name "Threads" threads-app.py
   ```

3. Find your executable at: `dist\Threads.exe`

## Creating a Desktop Shortcut

1. Navigate to the `dist` folder
2. Right-click on `Threads.exe`
3. Select "Send to" → "Desktop (create shortcut)"

## Troubleshooting

### Python not found
- Download and install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### PyInstaller command not found
Use the Python module syntax:
```
python -m PyInstaller --onefile --windowed --name "Threads" threads-app.py
```

### Import errors when running the .exe
Try building with hidden imports:
```
python -m PyInstaller --onefile --windowed --name "Threads" --hidden-import=webview threads-app.py
```

### WebView2 not available
- WebView2 should be pre-installed on Windows 10/11
- If not, download from: https://developer.microsoft.com/en-us/microsoft-edge/webview2/

## Project Structure

- `threads-app.py` - Main Python application
- `build-threads-app.ps1` - PowerShell build script
- `build-threads-app.bat` - Batch file build script
- `dist/Threads.exe` - Generated executable (after build)

## Configuration

The app saves window settings in: `%USERPROFILE%\.threads-app\window-config.json`

This includes:
- Window width and height
- Window position (x, y coordinates)

## License

This is a simple wrapper application for accessing Threads. All content and trademarks belong to their respective owners.
