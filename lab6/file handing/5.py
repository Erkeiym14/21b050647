s = list(str(input()))
with open('input1.txt', 'w') as f:
    for x in s:
        f.write(x + '\n')
