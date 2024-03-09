import re
s=str(input()) 
words = re.findall('[A-Z][a-z]*', s)
for x in words[0:]:
    print(x, end=" ")