def histogram(a):
    for i in a:
        print(i * '*')

list = [int(i) for i in input().split()]
print(histogram(list))