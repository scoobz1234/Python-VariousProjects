# -*- mode: python -*-

block_cipher = None


a = Analysis(['Git_Handler.py'],
             pathex=['/home/stephen/Desktop/cs114'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Git_Handler',
          debug=False,
          strip=False,
          upx=True,
          console=True )
