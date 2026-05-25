arr = list(map(int, input("Enter the elements of the array: ").split()))

if not arr:
    print("The array is empty.")
else:
    # Separate non-zero elements and zeros
    non_zeros = [x for x in arr if x != 0]
    zeros = [x for x in arr if x == 0]

    # Concatenate the two lists
    result = non_zeros + zeros

    print("The array after moving all zeros to the end is:", result)