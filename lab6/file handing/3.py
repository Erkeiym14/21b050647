import os

def test_path(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return
    
    filename = os.path.basename(path)
    directory = os.path.dirname(path)

    print(f"Path '{path}' exists.")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")

path = '/Users/erkemusss/Desktop/pp2/lab6/file handing'
test_path(path)
