print("Enter a number: ")
num = int(input())

reverse = 0
original = num

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number: ", reverse)

if reverse == original:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")