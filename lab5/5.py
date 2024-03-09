import re 
def func(string):
    patterns = 'a.*?b$'# *? matches the previous token between zero and unlimited times, as few times as possible, expanding as needed (lazy)
    if re.search(patterns, string):
        return "It is matched"
    else:
        return "It is not matched!"
    
print(func("aabbCbbb"))
print(func("aabAbbb"))
print(func("Aaababbbc"))
print(func("aaababbb"))
print(func("AaabAbbc"))
print(func("abb"))
print(func("abbhkaab"))
print(func("cab"))
print(func("afgthyfghb"))