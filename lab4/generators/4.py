def squares():
    i = 1
    while True:
        yield i*i
        i += 1 

a = int(input())
b = int(input())
for num in squares():
    if num in range(a, b):
        print(num)
     
    
n=int(input())
a=range(n)
print(list(a)[::-1])