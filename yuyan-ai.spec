# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

block_cipher = None

# 项目根目录
root_dir = Path(SPECPATH)

a = Analysis(
    ['main.py'],
    pathex=[str(root_dir)],
    binaries=[],
    datas=[
        ('config', 'config'),
        ('assets', 'assets'),
    ],
    hiddenimports=[
        'PyQt6.sip',
        'src.core',
        'src.ui',
    ],
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
    name='语嫣AI员工管家',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico' if sys.platform == 'win32' else 'assets/icon.icns',
)

# macOS app bundle
if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='语嫣AI员工管家.app',
        icon='assets/icon.icns',
        bundle_identifier='com.yuyanai.employee-manager',
        info_plist={
            'CFBundleShortVersionString': '1.0.0',
            'CFBundleVersion': '1.0.0',
            'NSHighResolutionCapable': 'True',
        },
    )
