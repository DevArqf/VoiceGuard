@echo off
REM VoiceGuard Windows Build Script
REM This script builds the VoiceGuard Windows executable

echo ========================================
echo   VoiceGuard Windows Build Script
echo ========================================
echo.

REM Check if Python is available
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X Python not found! Please install Python 3.8 or higher.
    pause
    exit /b 1
)
echo √ Python found
echo.

REM Install build dependencies
echo [2/5] Installing build dependencies...
pip install -r requirements-build.txt
if %errorlevel% neq 0 (
    echo X Failed to install build dependencies!
    pause
    exit /b 1
)
echo √ Build dependencies installed
echo.

REM Install application dependencies
echo [3/5] Installing application dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo X Failed to install application dependencies!
    pause
    exit /b 1
)
echo √ Application dependencies installed
echo.

REM Clean previous build
echo [4/5] Cleaning previous build...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
echo √ Cleaned previous build
echo.

REM Build executable
echo [5/5] Building VoiceGuard executable...
pyinstaller VoiceGuard.spec --clean
if %errorlevel% neq 0 (
    echo X Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Build Complete!
echo ========================================
echo.
echo Executable location: .\dist\VoiceGuard.exe
echo.
echo Next steps:
echo 1. Create a .env file in the same directory as VoiceGuard.exe
echo 2. Add your OPENAI_API_KEY to the .env file
echo 3. Run VoiceGuard.exe
echo.
pause
