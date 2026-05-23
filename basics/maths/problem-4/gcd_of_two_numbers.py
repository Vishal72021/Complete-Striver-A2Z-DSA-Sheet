print("Enter two numbers: ")
a = int(input())
b = int(input())

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD of the two numbers is: ", a)