import os
from shutil import copytree

folder = 'my_project/'
src = 'my_project/templates/'

for root, dirs, files in os.walk(folder):
    if 'templates' in dirs:
        idx = dirs.index('templates')
        path = os.path.join(root, dirs[idx])
        copytree(path, src, dirs_exist_ok=True)
