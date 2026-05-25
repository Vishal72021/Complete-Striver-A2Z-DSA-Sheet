arr = list(map(int, input("Enter the elements of the array: ").split()))
n = len(arr)

expected_sum = n * (n + 1) // 2

actual_sum = sum(arr)

missing_number = expected_sum - actual_sum

print("The missing number is:", missing_number)