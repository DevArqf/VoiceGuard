# VoiceGuard Windows Build Script
# This script builds the VoiceGuard Windows executable

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  VoiceGuard Windows Build Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is available
Write-Host "[1/5] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

# Install build dependencies
Write-Host ""
Write-Host "[2/5] Installing build dependencies..." -ForegroundColor Yellow
pip install -r requirements-build.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to install build dependencies!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Build dependencies installed" -ForegroundColor Green

# Install application dependencies
Write-Host ""
Write-Host "[3/5] Installing application dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to install application dependencies!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Application dependencies installed" -ForegroundColor Green

# Clean previous build
Write-Host ""
Write-Host "[4/5] Cleaning previous build..." -ForegroundColor Yellow
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist"
    Write-Host "✓ Removed dist folder" -ForegroundColor Green
}
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
    Write-Host "✓ Removed build folder" -ForegroundColor Green
}

# Build executable
Write-Host ""
Write-Host "[5/5] Building VoiceGuard executable..." -ForegroundColor Yellow
pyinstaller VoiceGuard.spec --clean
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Build failed!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Build Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Executable location: .\dist\VoiceGuard.exe" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Create a .env file in the same directory as VoiceGuard.exe" -ForegroundColor White
Write-Host "2. Add your OPENAI_API_KEY to the .env file" -ForegroundColor White
Write-Host "3. Run VoiceGuard.exe" -ForegroundColor White
Write-Host ""
