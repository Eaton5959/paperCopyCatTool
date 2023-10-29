# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app_for_text_copy_format.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app_for_text_copy_format',
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
    icon=['awsnh-2337s.icns'],
)
app = BUNDLE(
    exe,
    name='app_for_text_copy_format.app',
    icon='awsnh-2337s.icns',
    bundle_identifier=None,
)
