# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Collect all data files
added_files = [
    ('.env.example', '.'),
]

# Hidden imports that PyInstaller might miss
hidden_imports = [
    'openai',
    'pyaudio',
    'numpy',
    'scipy',
    'librosa',
    'soundfile',
    'speech_recognition',
    'dotenv',
    'matplotlib',
    'sklearn',
    'scipy.signal',
    'scipy.spatial',
    'librosa.core',
    'librosa.feature',
    'soundfile._soundfile_data',
    'pkg_resources.py2_warn',
    'tkinter',
    'tkinter.ttk',
    'tkinter.messagebox',
    'tkinter.simpledialog',
]

a = Analysis(
    ['main_gui.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='VoiceGuard-GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window for GUI
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon path here if you have one: icon='icon.ico'
)
