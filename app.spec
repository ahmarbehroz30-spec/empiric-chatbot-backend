# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('index.html', '.'), ('logo.png', '.'), ('main image.jfif', '.'), ('industrial cables.jfif', '.'), ('raw materials.jfif', '.'), ('Valves & Actuators.jfif', '.'), ('Steel & Metal Sheets.jfif', '.'), ('Lubricants & Oils.jfif', '.'), ('Electrical Switchgears.jfif', '.'), ('Hardware & Toolkits.jfif', '.'), ('Metal Pipings & Sections.jfif', '.'), ('image_40c27e.png', '.'), ('image_40c926.png', '.'), ('image_40c61c.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
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
)
