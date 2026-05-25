arr = list(map(int, input("Enter the elements of the sorted array: ").split()))

if not arr:
    print("The array is empty.")
else:
    unique_elements = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_elements.append(arr[i])

    print("The array with duplicates removed is:", unique_elements)