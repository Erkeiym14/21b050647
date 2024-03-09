import re 
def func(string):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns, string):
        return "It is matched"
    else:
        return "It is not matched!"
    
print(func("aabbCbbbc"))
print(func("aabAbbbc"))
print(func("Aaababbbc"))
print(func("aaababbbc"))
print(func("AaabAbbc"))
print(func("abab"))
print(func("abbaa"))
print(func("ca"))
print(func("AA"))