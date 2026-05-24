print("Enter the number of elements in the array: ")
n = int(input())

arr = []
print("Enter the elements of the array: ")
for i in range(n):
    element = int(input())
    arr.append(element)

freq = {}

for element in arr:
    if element in freq:
        freq[element] += 1
    else:
        freq[element] = 1

for element, count in freq.items():
    print(f"Element {element} occurs {count} times.")