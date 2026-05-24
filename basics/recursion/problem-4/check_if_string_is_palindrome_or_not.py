print("Enter a string: ")
s = input()

def is_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left+1, right-1)

if is_palindrome(s, 0, len(s)-1):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")