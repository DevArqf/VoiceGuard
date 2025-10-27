# 🔨 Building VoiceGuard for Windows

This guide explains how to build VoiceGuard into a standalone Windows executable (.exe file) that can run without requiring Python to be installed.

## 📋 Prerequisites

Before building, ensure you have:

- **Python 3.8 or higher** installed on your system
- **All dependencies** from `requirements.txt` installed
- **PyInstaller** for building the executable
- **At least 2GB of free disk space** for the build process

## 🚀 Quick Build

### Option 1: Using PowerShell (Recommended)

```powershell
.\build.ps1
```

### Option 2: Using Batch Script

```batch
build.bat
```

### Option 3: Manual Build

```bash
# Install build dependencies
pip install -r requirements-build.txt

# Install application dependencies
pip install -r requirements.txt

# Build the executable
pyinstaller VoiceGuard.spec --clean
```

## 📦 Build Output

After a successful build, you'll find:

- **Executable**: `dist\VoiceGuard.exe`
- **Build files**: `build\` directory (can be deleted)
- **Temporary files**: `__pycache__` directories (can be deleted)

## 🎯 Distribution

To distribute VoiceGuard to other users:

1. **Copy these files** to a distribution folder:
   - `dist\VoiceGuard.exe` (the main executable)
   - `.env.example` (rename to `.env` and add API key)

2. **Create a README** with setup instructions:
   ```
   1. Rename .env.example to .env
   2. Open .env in a text editor
   3. Add your OpenAI API key: OPENAI_API_KEY=sk-...
   4. Run VoiceGuard.exe
   ```

3. **Optional**: Create a ZIP file with all necessary files

## 🔧 Customization

### Adding an Icon

1. Create or download a `.ico` file for VoiceGuard
2. Save it as `icon.ico` in the project root
3. Edit `VoiceGuard.spec` and change:
   ```python
   icon=None,  # Change this
   ```
   to:
   ```python
   icon='icon.ico',
   ```
4. Rebuild the executable

### Changing Build Settings

Edit `VoiceGuard.spec` to customize:

- **Console Window**: Set `console=False` for no console window (GUI mode)
- **Single File**: Already configured for single file output
- **Hidden Imports**: Add any missing modules to `hidden_imports` list
- **Data Files**: Add additional files to `added_files` list

## 🐛 Troubleshooting

### Build Fails with Import Errors

**Solution**: Add missing modules to `hidden_imports` in `VoiceGuard.spec`:
```python
hidden_imports = [
    'openai',
    'pyaudio',
    # Add your missing module here
    'your_missing_module',
]
```

### Executable Crashes on Startup

**Solution**: 
1. Run the executable from command line to see error messages
2. Ensure all required DLLs are included (especially for PyAudio)
3. Check that `.env` file is in the same directory as the executable

### Large File Size

The executable may be 200-500MB due to included libraries. This is normal for PyInstaller builds with scientific libraries (NumPy, SciPy, librosa).

**To reduce size**:
- Use UPX compression (already enabled in spec file)
- Remove unused dependencies from `requirements.txt`
- Use PyInstaller's `--exclude-module` option for unnecessary modules

### Missing Audio Libraries

**For PyAudio on Windows**:
```bash
pip install pipwin
pipwin install pyaudio
```

### OpenAI API Key Issues

The executable will look for a `.env` file in:
1. The same directory as the executable
2. The current working directory

Make sure users place the `.env` file next to `VoiceGuard.exe`.

## 🔍 Verifying the Build

Test the executable:

1. **Check if it runs**:
   ```bash
   .\dist\VoiceGuard.exe --config-check
   ```

2. **Test on a clean Windows machine** (without Python installed)

3. **Verify all features work**:
   - User enrollment
   - Voice identification
   - Microphone testing
   - Database operations

## 📝 Build Script Details

### What the Build Script Does

1. ✅ Checks Python installation
2. 📦 Installs PyInstaller (build tool)
3. 📦 Installs application dependencies
4. 🧹 Cleans previous build artifacts
5. 🔨 Compiles Python code to executable
6. 📁 Creates distribution folder with executable

### Build Time

Typical build time: **2-5 minutes** depending on your system.

## 🌐 Cross-Platform Notes

This build process creates a **Windows-only** executable. For other platforms:

- **macOS**: Run the build script on macOS (PyInstaller will create `.app`)
- **Linux**: Run the build script on Linux (PyInstaller will create Linux binary)

PyInstaller creates platform-specific executables, so you need to build on each target platform.

## 📞 Support

If you encounter issues:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review PyInstaller documentation: https://pyinstaller.org/
3. Open an issue on GitHub with:
   - Error messages
   - Python version
   - Windows version
   - Build log output

## 🎉 Success!

Once built successfully, you can:

- ✅ Run VoiceGuard without Python installed
- ✅ Distribute to other Windows users
- ✅ Deploy to production Windows environments
- ✅ Create desktop shortcuts for easy access

---

**Next Steps**: After building, see [DISTRIBUTION.md](DISTRIBUTION.md) for how to package and distribute VoiceGuard to end users.
