# 🪟 VoiceGuard Windows Executable - Quick Guide

## 🚀 Quick Build

To build VoiceGuard as a Windows .exe file:

### Using PowerShell
```powershell
.\build.ps1
```

### Using Batch Script
```batch
build.bat
```

## 📦 Output

After building, you'll find:
- **Executable**: `dist\VoiceGuard.exe` (standalone application)
- **Size**: Approximately 200-400 MB

## 🎯 Running the Executable

### First Time Setup

1. **Create .env file** in the same directory as VoiceGuard.exe:
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   ```

2. **Run the executable**:
   ```
   .\dist\VoiceGuard.exe
   ```

### For End Users

When distributing to users without Python:

1. Copy `dist\VoiceGuard.exe` to a folder
2. Copy `.env.example` to the same folder
3. Rename `.env.example` to `.env`
4. Add OpenAI API key to `.env`
5. Double-click `VoiceGuard.exe`

## ✅ Testing

Test the build:
```powershell
.\dist\VoiceGuard.exe --config-check
```

## 📚 More Information

- **Build Documentation**: See [BUILD.md](BUILD.md)
- **Distribution Guide**: See [DISTRIBUTION.md](DISTRIBUTION.md)
- **Main README**: See [README.md](README.md)

## ⚡ Features of the Executable

✅ No Python installation required
✅ Single file distribution
✅ Works on any Windows 10+ machine
✅ Includes all dependencies
✅ Same features as the Python version

## 🐛 Troubleshooting

**Issue**: "OPENAI_API_KEY not configured"
- Ensure `.env` file is in the same directory as the .exe
- Check the API key is correctly formatted

**Issue**: Executable won't run
- Run from Command Prompt to see error messages
- Check Windows Defender hasn't blocked it
- Verify you have a working microphone

**Issue**: Large file size
- This is normal for PyInstaller builds with scientific libraries
- Size: 200-400 MB is expected

## 💡 Tips

- Keep `.env` file in the same directory as VoiceGuard.exe
- Database files are created automatically in a `data\` folder
- You can move VoiceGuard.exe to any location, just bring the `.env` file with it

---

**Need help?** Check [BUILD.md](BUILD.md) for detailed instructions or [open an issue](https://github.com/DevArqf/VoiceGuard/issues).
