# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['crawl.py'],
             pathex=['D:\\Synology_Sync\\SynologyDrive\\脚本\\JavSpider'],
             binaries=[],
             datas=[('mime.types', 'scrapy'), ('VERSION', 'scrapy'), ('JavSpider/*py', 'JavSpider'), ('JavSpider/spiders/*.py', 'JavSpider/spiders')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=['generate_cfg.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='crawl',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
