def palindrome(s):
    if s == s[::-1]:
        return "This is a palindrome"
    return "This is not a palindrome"

s1 = str(input())
is_palindrome = palindrome(s1)
print(is_palindrome)