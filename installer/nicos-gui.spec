# -*- mode: python -*-

import sys
from os import path

sys.path.insert(0, path.abspath('.'))

from utils import rootdir, find_uis, find_custom, find_gr, find_modules, find_resources

binscript = path.join(rootdir, 'bin', 'nicos-gui')


a = Analysis([binscript],
             pathex=[rootdir],
             binaries=[],
             datas=find_uis() + find_custom() + find_gr() + find_resources() + [
                 (path.join(rootdir, 'nicos', 'RELEASE-VERSION'), 'nicos')],
             hiddenimports=
                 find_modules('nicos', 'clients', 'gui') +
                 find_modules('nicos', 'clients', 'flowui') +
                 find_modules('nicos', 'guisupport') +
                 find_modules('nicos', 'core') +
                 find_modules('nicos', 'devices'),
             hookspath=[],
             excludes=['Tkinter', 'matplotlib', 'gtk', 'IPython',
                       'ipykernel', 'pygments'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=None)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='nicos-gui',
          debug=False,
          strip=False,
          console=False)
