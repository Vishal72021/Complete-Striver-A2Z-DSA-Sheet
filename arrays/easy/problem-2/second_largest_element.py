print("Enter the number of elements in the array: ")
n = int(input())

print("Enter the elements of the array: ")
arr = list(map(int, input().split()))

if n < 2:
    print("Array does not have enough elements")
else:
    largest = arr[0]
    second_largest = arr[1]

    if second_largest > largest:
        largest, second_largest = second_largest, largest

    for i in range(2, n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    print("The second largest element in the array is:", second_largest)