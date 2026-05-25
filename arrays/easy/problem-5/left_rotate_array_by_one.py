arr = list(map(int, input("Enter the elements of the array: ").split()))

if len(arr) <= 1:
    print("The array is already rotated.")
else:
    first_element = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[-1] = first_element

    print("The array after left rotation by one position is:", arr)