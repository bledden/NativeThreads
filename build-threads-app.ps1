# Build script for Threads Native App
# This script should be run in Windows PowerShell

Write-Host "Building Threads Native App for Windows..." -ForegroundColor Cyan

# Check if Python is installed
try {
    $pythonVersion = python --version 2>$null
    Write-Host "Found Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Install dependencies
Write-Host "`nInstalling dependencies..." -ForegroundColor Yellow
pip install pywebview pyinstaller

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Build the executable
Write-Host "`nBuilding executable..." -ForegroundColor Yellow
python -m PyInstaller --onefile --windowed --name "Threads" --icon="threads.ico" threads-app.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to build executable" -ForegroundColor Red
    exit 1
}

# Check if build was successful
if (Test-Path ".\dist\Threads.exe") {
    Write-Host "`nBuild successful!" -ForegroundColor Green
    Write-Host "Executable location: .\dist\Threads.exe" -ForegroundColor Cyan
    
    # Create desktop shortcut automatically
    Write-Host "`nCreating desktop shortcut..." -ForegroundColor Yellow
    try {
        $desktop = [Environment]::GetFolderPath("Desktop")
        $WshShell = New-Object -comObject WScript.Shell
        $Shortcut = $WshShell.CreateShortcut("$desktop\Threads.lnk")
        $Shortcut.TargetPath = (Get-Item ".\dist\Threads.exe").FullName
        $Shortcut.WorkingDirectory = (Get-Item ".\dist").FullName
        $Shortcut.IconLocation = (Get-Item ".\dist\Threads.exe").FullName
        $Shortcut.Save()
        Write-Host "Desktop shortcut created at: $desktop\Threads.lnk" -ForegroundColor Green
    } catch {
        Write-Host "Warning: Could not create desktop shortcut automatically" -ForegroundColor Yellow
        Write-Host "You can manually create a shortcut to: $(Get-Item '.\dist\Threads.exe').FullName" -ForegroundColor Yellow
    }
    
    # Ask if user wants to run the app
    $runApp = Read-Host "`nRun Threads app now? (y/n)"
    if ($runApp -eq 'y') {
        Start-Process ".\dist\Threads.exe"
    }
} else {
    Write-Host "Error: Executable not found in dist folder" -ForegroundColor Red
    exit 1
}

Write-Host "`nDone!" -ForegroundColor Green