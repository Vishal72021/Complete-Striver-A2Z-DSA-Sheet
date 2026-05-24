def sum_of_natural_numbers(n):
    if n <= 1:
        return n
    return n + sum_of_natural_numbers(n - 1)

print("Enter a number: ")
n = int(input())

sum_of_natural_numbers_result = sum_of_natural_numbers(n)
print("Sum of the first", n, "natural numbers is:", sum_of_natural_numbers_result)