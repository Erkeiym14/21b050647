s = str(input())
upper = 0
lower = 0

for x in s:
    if 65 <=ord(x)<=90:
        upper = upper+1
    elif 97 <= ord(x) <= 122:
        lower = lower+1
print( "UPPER: ", upper)
print("LOWER: ", lower)