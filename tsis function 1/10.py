def unique_elements(a):
    x = []
    for b in a:
        if b not in x:
            x.append(b)
    return x

list = [int(i) for i in input().split()]
print(unique_elements(list))