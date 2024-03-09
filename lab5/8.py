import re
s = str(input())
x = re.findall('[A-Z][^A-Z]*', s)
print(x)