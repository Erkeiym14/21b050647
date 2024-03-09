import os
path_dir = '/Users/erkemusss/Desktop/pp2/lab6/file handing'
if os.path.exists(path_dir):
    print("Yes")
    os.remove(path_dir)
else:
    print("No")
