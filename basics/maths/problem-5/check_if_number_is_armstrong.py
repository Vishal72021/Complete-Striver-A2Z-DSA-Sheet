print("Enter a number: ")
num = int(input())

order = len(str(num))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")