# bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Enter the number of elements in the array: ")
n = int(input())

arr = []

print("Enter the elements of the array: ")
for i in range(n):
    element = int(input())
    arr.append(element)

bubble_sort(arr)
print("Sorted array: ", arr)