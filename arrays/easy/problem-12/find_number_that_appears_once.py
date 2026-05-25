arr = list(map(int, input("Enter the elements of the array: ").split()))

result = 0
for num in arr:
    result ^= num

print("The number that appears once is:", result)