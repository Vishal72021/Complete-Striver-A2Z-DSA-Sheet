arr = list(map(int, input("Enter the elements of the array: ").split()))
is_sorted = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

print("The array is sorted." if is_sorted else "The array is not sorted.")