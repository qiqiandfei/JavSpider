# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['crawl.py'],
    pathex=['C:\\Users\\fyu\\Desktop\\JavSpider'],
    binaries=[],
    datas=[('JavSpider\\items.py', 'JavSpider'),
        ('JavSpider\\middlewares.py', 'JavSpider'),
        ('JavSpider\\pipelines.py', 'JavSpider'),
        ('JavSpider\\settings.py', 'JavSpider'),
        ('JavSpider\\spiders\\*.py', 'JavSpider/spiders'),
        ('.\\*.py', 'JavSpider')],
    hiddenimports=['scrapy',
        'JavSpider.settings',
        'JavSpider.spiders'],
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
    name='javspider_win_amd64',
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
