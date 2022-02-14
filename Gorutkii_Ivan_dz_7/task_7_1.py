import os

dirs = ('settings', 'mainapp', 'adminapp', 'authapp')
root_name = 'my_project'

for dir in dirs:
    dir_path = os.path.join(root_name, dir)
    print(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
