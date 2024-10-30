import sys
from PyInstaller.utils import hooks

# Add the path to the PyQt5 plugins folder
qt5_plugins_dir = hooks.collect_data_files('PyQt5')[0][1]

a = Analysis(['yeahfu.py'],
             pathex=['.'],
             binaries=[],
             datas=[('overlay_image.jpg', '.')],  # Include the overlay image
             hiddenimports=[qt5_plugins_dir],
             hookspath=[],
             runtime_hooks=[],
             excludes=[])

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='myapp',
          debug=False,
          strip=False,
          upx=True)