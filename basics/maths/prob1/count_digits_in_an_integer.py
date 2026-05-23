print("Enter a number: ")
n = int(input())

count = 0
while n > 0:
    count += 1
    n = n // 10

print("Number of digits: ", count)