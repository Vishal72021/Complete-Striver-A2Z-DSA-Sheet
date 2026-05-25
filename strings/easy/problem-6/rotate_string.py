print("Enter a string: ")
s = input()
print("Enter the number of positions to rotate: ")
k = int(input())

k = k % len(s)
rotated = s[k:] + s[:k]

print("The rotated string is:", rotated)