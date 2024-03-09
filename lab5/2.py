import re 
def func(string):
    patterns = 'ab{2,3}'
    if re.search(patterns, string):
        return "It is matched"
    else:
        return "It is not matched!"
    
print(func("acc"))
print(func("abbbcc"))
print(func("aaa"))
print(func("abbaab"))
print(func("abb"))
print(func("abab"))
print(func("abbaa"))
print(func("cab"))
print(func("aabb"))