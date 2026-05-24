def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Enter a number: ")
n = int(input())

result = factorial(n)

print("Factorial of the number is: ", result)