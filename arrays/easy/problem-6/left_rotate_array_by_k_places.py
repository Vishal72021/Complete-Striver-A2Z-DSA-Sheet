arr = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter the number of positions to rotate: "))

if len(arr) <= 1:
    print("The array is already rotated.")
else:
    k = k % len(arr)
    rotated = arr[k:] + arr[:k]
    print("The array after left rotation by", k, "positions is:", rotated)