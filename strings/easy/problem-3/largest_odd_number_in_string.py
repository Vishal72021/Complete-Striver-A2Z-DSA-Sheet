print("Enter a string of digits: ")
s = input()

largest_odd = -1

for char in s:
    if char.isdigit():
        digit = int(char)
        if digit % 2 == 1 and digit > largest_odd:
            largest_odd = digit

if largest_odd == -1:
    print("No odd number found.")
else:
    print("The largest odd number in the string is:", largest_odd)