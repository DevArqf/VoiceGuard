# 🚀 VoiceGuard GUI - Quick Start Guide

Get started with VoiceGuard's graphical interface in just a few minutes!

## ⚡ 3-Step Setup

### 1. Run the Application

**From Source:**
```bash
python main_gui.py
```

**From Executable:**
- Double-click `VoiceGuard-GUI.exe`

### 2. Configure API Key

If you see a configuration error:

1. Create a file named `.env` in the same folder as the app
2. Add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   ```
3. Click "Retry" in the application

### 3. Test Your Setup

1. Click **"🎤 Test Microphone"**
2. Follow the prompts to verify your mic works
3. You're ready to enroll users!

## 🎯 First Steps

### Enroll Your First User

1. Click **"📝 Enroll New User"** on the home screen
2. Enter a username (e.g., "john_doe")
3. Click **"Start Enrollment"**
4. Record 3 voice samples when prompted
5. Wait for confirmation ✅

### Verify the User

1. Click **"🔍 Verify User"**
2. Enter the username you just enrolled
3. Click **"Start Verification"**
4. Speak when prompted
5. See your confidence score!

## 🖱️ Main Features

```
Home Screen:
┌────────────────────────────┐
│  📝 Enroll New User        │  → Register voices
│  🔍 Verify User            │  → Check identity
│  🎯 Identify Speaker       │  → Find who's speaking
│  👥 Manage Users           │  → View/delete users
│  🎤 Test Microphone        │  → Check audio
│  📊 System Stats           │  → View metrics
└────────────────────────────┘
```

## 💡 Tips for Best Results

### ✅ DO:
- Use a quiet room
- Speak naturally
- Use the same microphone
- Speak for the full duration
- Test microphone first

### ❌ DON'T:
- Whisper or shout
- Use in noisy environments
- Switch microphones
- Speak too briefly
- Skip microphone testing

## 🐛 Common Issues

### "Configuration Error"
- **Fix**: Create `.env` file with your API key

### "Audio too quiet"
- **Fix**: Check microphone settings, speak louder

### "User not found"
- **Fix**: Enroll the user first

### App doesn't start
- **Fix**: Run `python main_gui.py` to see errors

## 📚 Learn More

- **Full GUI Guide**: [GUI.md](GUI.md)
- **Build Instructions**: [BUILD.md](BUILD.md)
- **Main README**: [README.md](README.md)

## 🎬 Typical Workflow

```
1. Launch App
   ↓
2. Test Microphone ✓
   ↓
3. Enroll Users (repeat for each)
   ↓
4. Verify Users (authenticate)
   ↓
5. View Statistics
```

## 🔧 Configuration

Optional: Edit `.env` to customize:

```env
SAMPLE_RATE=16000          # Audio quality
RECORD_SECONDS=5           # Recording length
SIMILARITY_THRESHOLD=0.8   # Match sensitivity
```

## 📊 Understanding Results

**Confidence Score Meanings:**
- 🟢 90-100%: Excellent match
- 🟢 80-89%: Good match
- 🟡 70-79%: Acceptable match
- 🔴 <70%: Poor match (fails)

## 🎯 What's Next?

After getting started:

1. **Enroll multiple users** to test identification
2. **Check statistics** to see system performance
3. **Review user details** in the Manage Users section
4. **Build the executable** for distribution ([BUILD.md](BUILD.md))

## 🆘 Need Help?

- **Documentation**: Read [GUI.md](GUI.md)
- **Issues**: Check error messages in the app
- **Support**: Open a GitHub issue
- **API**: Verify your OpenAI API key is active

---

**Ready?** Launch VoiceGuard and start securing with voice! 🛡️

**Made with ❤️ by DevArqf**
