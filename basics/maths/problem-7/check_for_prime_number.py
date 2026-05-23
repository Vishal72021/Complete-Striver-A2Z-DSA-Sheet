print("Enter a number: ")
n = int(input())

is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")