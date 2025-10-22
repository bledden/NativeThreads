# Threads Native App for Windows and macOS

A native desktop application that displays Threads (https://www.threads.com) in a dedicated window without browser UI. Available for both Windows and macOS.

This was coded entirely by claude and only audited for security leaks. Just a fun little exercise to address a minor pain point with my current favorite social media site. Have not cleaned-up or optimized a thing personally. Clone at your own risk!

## Features

- Native window without browser toolbar or navigation buttons
- Remembers window size and position between launches
- **Persistent login state** - stays logged in between app launches
- **Custom application icon** for both Windows and macOS
- Cross-platform support (Windows and macOS)
- Windows: Uses Microsoft Edge WebView2 for rendering
- macOS: Uses native WebKit for rendering
- Configuration and session data saved in `~/.threads-app/`

## Prerequisites

### Windows
- Windows 10 or Windows 11
- Python 3.7 or higher
- WebView2 runtime (usually pre-installed on modern Windows)

### macOS
- macOS 10.10 (Yosemite) or later
- Python 3.7 or higher
- Xcode Command Line Tools (for building)

## Quick Start

### Windows

#### Option 1: Using PowerShell (Recommended)
1. Open PowerShell as regular user (no admin required)
2. Navigate to this directory
3. Run: `.\build-threads-app.ps1`
4. The script will automatically create a desktop shortcut

#### Option 2: Using Command Prompt
1. Open Command Prompt
2. Navigate to this directory
3. Run: `build-threads-app.bat`
4. The script will automatically create a desktop shortcut

#### Option 3: Manual Build
1. Install dependencies:
   ```
   pip install pywebview pyinstaller
   ```

2. Build the executable:
   ```
   python -m PyInstaller --onefile --windowed --name "Threads" --icon="threads.ico" threads-app.py
   ```

3. Find your executable at: `dist\Threads.exe`

### macOS

#### Option 1: Using Build Script (Recommended)
1. Open Terminal
2. Navigate to this directory
3. Run: `./build-threads-app-macos.sh`
4. The script will automatically install the app to /Applications

#### Option 2: Manual Build
1. Create virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install pywebview py2app pillow
   ```

3. Build the app:
   ```
   python setup.py py2app
   ```

4. Find your app at: `dist/Threads.app`

5. (Optional) Copy to Applications:
   ```
   cp -r dist/Threads.app /Applications/
   ```

## Creating a Desktop Shortcut

### Windows
1. Navigate to the `dist` folder
2. Right-click on `Threads.exe`
3. Select "Send to" → "Desktop (create shortcut)"

### macOS
1. Open Finder and navigate to `dist/Threads.app`
2. Hold Option+Command and drag the app to your Desktop
3. Or simply copy the app to `/Applications` folder

## Troubleshooting

### Windows Issues

#### Python not found
- Download and install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

#### PyInstaller command not found
Use the Python module syntax:
```
python -m PyInstaller --onefile --windowed --name "Threads" threads-app.py
```

#### Import errors when running the .exe
Try building with hidden imports:
```
python -m PyInstaller --onefile --windowed --name "Threads" --icon="threads.ico" --hidden-import=webview threads-app.py
```

#### WebView2 not available
- WebView2 should be pre-installed on Windows 10/11
- If not, download from: https://developer.microsoft.com/en-us/microsoft-edge/webview2/

### macOS Issues

#### Xcode Command Line Tools not installed
Install with:
```
xcode-select --install
```

#### py2app build errors
Try cleaning and rebuilding:
```
rm -rf build dist
python setup.py py2app
```

#### App won't open (security warning)
- Right-click the app and select "Open"
- Or go to System Preferences → Security & Privacy → General
- Click "Open Anyway" for Threads.app

#### ImportError when running the app
Ensure all dependencies are included:
```
pip install --upgrade pywebview py2app
```

## Project Structure

- `threads-app.py` - Main Python application (cross-platform)
- `build-threads-app.ps1` - Windows PowerShell build script
- `build-threads-app.bat` - Windows batch file build script
- `build-threads-app-macos.sh` - macOS build script
- `setup.py` - macOS py2app configuration
- `threads.ico` - Windows application icon
- `threads.icns` - macOS application icon
- `requirements.txt` - Python dependencies
- `dist/Threads.exe` - Windows executable (after build)
- `dist/Threads.app` - macOS app bundle (after build)

## Configuration

The app saves data in:
- Windows: `%USERPROFILE%\.threads-app\`
- macOS: `~/.threads-app/`

This includes:
- `window-config.json` - Window size and position
- Browser session data - Cookies and local storage for persistent login

## License

This is a simple wrapper application for accessing Threads. All content and trademarks belong to their respective owners.
