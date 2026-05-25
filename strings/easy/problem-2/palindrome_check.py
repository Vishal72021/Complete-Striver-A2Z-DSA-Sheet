print("Enter a string: ")
s = input()

# Remove non-alphanumeric characters and convert to lowercase
s = ''.join(c.lower() for c in s if c.isalnum())

# Check if the string is equal to its reverse
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")