# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

block_cipher = None

# Collect all dependencies
tk_data = collect_all('tkinter')
pil_data = collect_all('PIL')

a = Analysis(
    ['main.pyw'],
    pathex=[],
    binaries=[],
    datas=[
        *tk_data[0],
        *pil_data[0],
        ('config/*.py', 'config'),
        ('core/*.py', 'core'),
        ('ui/*.py', 'ui'),
        ('ui/components/*.py', 'ui/components')
    ],
    hiddenimports=[
        *tk_data[2],  # tkinter hidden imports
        *pil_data[2],  # PIL hidden imports
        'tkinter',
        'tkinter.messagebox',
        'tkinter.ttk',
        'PIL',
        'PIL.Image'
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

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Vitalize',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='vitalize.ico',
    embed_manifest=True,
)
