import math
def sphere(r):
    volume = (4/3) * math.pi * pow(r, 3)
    return volume 

r = int(input())
print(sphere(r))