@echo off
echo Building Threads Native App for Windows...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Installing dependencies...
pip install pywebview pyinstaller
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Building executable...
python -m PyInstaller --onefile --windowed --name "Threads" threads-app.py
if errorlevel 1 (
    echo Error: Failed to build executable
    pause
    exit /b 1
)

if exist "dist\Threads.exe" (
    echo.
    echo Build successful!
    echo Executable location: dist\Threads.exe
    echo.
    echo You can now run the app by double-clicking dist\Threads.exe
    echo Or create a desktop shortcut by right-clicking on it and selecting "Send to" - "Desktop"
) else (
    echo Error: Executable not found in dist folder
)

echo.
pause