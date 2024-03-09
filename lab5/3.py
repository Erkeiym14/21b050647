import re 
def func(string):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, string):
        return "It is matched"
    else:
        return "It is not matched!"
    
print(func("aabb_Cbbbc"))
print(func("aab_Abbbc"))
print(func("Aaab_abbbc"))
print(func("aaab_abbbc"))
print(func("Aaab_Abbc"))
print(func("ab_ab"))
print(func("a_bbaa"))
print(func("ca_b"))
print(func("AA_AA"))