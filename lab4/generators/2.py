n = int(input())
divisibl = [i for i in range(0, n) if (i % 2 == 0)]
print(divisibl)

def divChecker(n):
    for i in range(n):
        if i % 2 == 0:
            print(i)

divChecker(n)