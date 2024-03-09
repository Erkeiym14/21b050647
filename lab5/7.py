import re
s = str(input())
x = re.sub("[_]", " ",s)
q = x.split(" ")
for w in q[0:]:
    print(w.title(),end="")