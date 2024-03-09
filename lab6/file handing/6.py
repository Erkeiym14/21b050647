import os
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in s:
    with open(x + ".txt", "w") as f:
        f.writelines(x)
