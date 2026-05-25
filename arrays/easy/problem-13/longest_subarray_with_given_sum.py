arr = list(map(int, input("Enter the elements of the array: ").split()))
target_sum = int(input("Enter the target sum: "))

prefix_sum = 0
sum_indices = {0: -1}  # Initialize with sum 0 at index -1
max_length = 0

for i, num in enumerate(arr):
    prefix_sum += num

    if prefix_sum == target_sum:
        max_length = i + 1
    elif prefix_sum - target_sum in sum_indices:
        length = i - sum_indices[prefix_sum - target_sum]
        max_length = max(max_length, length)

    if prefix_sum not in sum_indices:
        sum_indices[prefix_sum] = i

print("The length of the longest subarray with the given sum is:", max_length)