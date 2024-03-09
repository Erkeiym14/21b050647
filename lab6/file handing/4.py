with open('/Users/erkemusss/Desktop/pp2/lab6/file handing/input.txt', 'r') as file:
    lines = file.readlines()

num_lines = len(lines)
print(f"Number of lines in the file: {num_lines}")
