# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

def get_locales_data(): #(https://stackoverflow.com/questions/61718298/compiling-gettext-locales-with-pyinstaller-in-python-3-x)
    locales_data = []
    for locale in os.listdir(os.path.join('./locales')):
        if locale == "CONFIG":
            locales_data.append((os.path.join('./locales', locale, "config.py"),os.path.join('./locales', locale)))
            continue
        locales_data.append((
            os.path.join('./locales', locale, 'LC_MESSAGES/*.mo'),
            os.path.join('locales', locale, 'LC_MESSAGES'),
        ))
    return locales_data

a = Analysis(['palc.py'],
             pathex=['/home/thetechrobo/python-text-calculator'],
             binaries=[],
             datas=get_locales_data(),
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
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
          name='palc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
