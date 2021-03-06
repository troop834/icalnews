# -*- mode: python ; coding: utf-8 -*-

##
## icalnews - icalnews.spec
##
## Copyright (C) 2022 Kian Kasad
##
## This file is made available under a modified BSD license.
## See the accompanying LICENSE file for details.
##

block_cipher = None


a = Analysis(
    ['icalnews.py'],
    pathex=[],
    binaries=[],
    datas=[('template.html', '.')],
    hiddenimports=[],
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
    name='icalnews',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# vim: ft=python
