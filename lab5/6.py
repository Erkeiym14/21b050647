import re
n = str(input())
print(re.sub("[ ,.]", ":", n))