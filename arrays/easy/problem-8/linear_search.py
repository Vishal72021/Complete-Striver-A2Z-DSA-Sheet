arr = list(map(int, input("Enter the elements of the array: ").split()))
target = int(input("Enter the element to search for: "))

found = False
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element {target} found at index {i}")
        found = True
        break

if not found:
    print(f"Element {target} not found in the array")