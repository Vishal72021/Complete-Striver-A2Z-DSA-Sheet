print("Enter the number of elements in the array: ")
n = int(input())
arr = []
print("Enter the elements of the array: ")
for i in range(n):
    element = int(input())
    arr.append(element)

hash_map = {}
max_count = 0
highest_occuring_element = None

for element in arr:
    if element in hash_map:
        hash_map[element] += 1
    else:
        hash_map[element] = 1

    if hash_map[element] > max_count:
        max_count = hash_map[element]
        highest_occuring_element = element

print("The highest occurring element is: ", highest_occuring_element)