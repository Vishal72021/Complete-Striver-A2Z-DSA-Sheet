def recursive_bubble_sort(arr, n):
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    recursive_bubble_sort(arr, n - 1)

print("Enter the number of elements in the array: ")
n = int(input())

arr = []

print("Enter the elements of the array: ")
for i in range(n):
    element = int(input())
    arr.append(element)

recursive_bubble_sort(arr, n)
print("Sorted array: ", arr)