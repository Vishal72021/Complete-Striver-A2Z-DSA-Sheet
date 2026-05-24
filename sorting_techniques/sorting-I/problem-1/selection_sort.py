def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

print("Enter the number of elements in the array: ")
n = int(input())

arr = []

print("Enter the elements of the array: ")
for i in range(n):
    element = int(input())
    arr.append(element)

selection_sort(arr)
print("Sorted array: ", arr)