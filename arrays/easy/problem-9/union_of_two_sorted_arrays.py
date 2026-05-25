arr1 = list(map(int, input("Enter the elements of the first sorted array: ").split()))
arr2 = list(map(int, input("Enter the elements of the second sorted array: ").split()))

if not arr1 and not arr2:
    print("Both arrays are empty.")
elif not arr1:
    print("The union of the two arrays is:", arr2)
elif not arr2:
    print("The union of the two arrays is:", arr1)
else:
    union = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            i += 1
            j += 1

    union.extend(arr1[i:])
    union.extend(arr2[j:])

    print("The union of the two sorted arrays is:", union)