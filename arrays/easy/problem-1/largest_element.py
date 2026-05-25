print("Enter the number of elements in the array: ")
n = int(input())

print("Enter the elements of the array: ")
arr = list(map(int, input().split()))

largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print("The largest element in the array is:", largest)