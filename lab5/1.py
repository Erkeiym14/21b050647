import re
def func(string):
    patterns = '^a(b*)$'
    if re.search(patterns, string):
        return "It is matched"
    else:
        return "It is not matched!"

print(func("ac"))
print(func("abc"))
print(func("a"))
print(func("ab"))
print(func("abb"))
print(func("abab"))
print(func("abbaa"))
print(func("cab"))
print(func("aabb"))