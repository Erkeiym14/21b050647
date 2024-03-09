import os

def check_access(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return
    
    if not os.access(path, os.R_OK):
        print(f"Path '{path}' is not readable.")

    if not os.access(path, os.W_OK):
        print(f"Path '{path}' is not writable.")
    
    if not os.access(path, os.X_OK):
        print(f"Path '{path}' is not executable.")

path = '/Users/erkemusss/Desktop/pp2/lab6/file handing'
check_access(path)
