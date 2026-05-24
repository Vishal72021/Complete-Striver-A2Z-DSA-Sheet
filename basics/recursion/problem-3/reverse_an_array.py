def reverse_array(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverse_array(arr, start + 1, end - 1)

print("Enter a number: ")
n = int(input())

arr = []

print("Enter the elements of the array: ")
for i in range(n):
    element = int(input())
    arr.append(element)

reverse_array(arr, 0, n - 1)

print("Reversed array: ", arr)