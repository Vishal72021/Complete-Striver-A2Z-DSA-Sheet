print("Enter a number: ")
n = int(input())

print("Divisors of the number are: ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)