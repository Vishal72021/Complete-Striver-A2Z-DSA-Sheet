print("Enter a list of strings: ")
strings = input().split()

if not strings:
    print("No strings provided.")
else:
    prefix = ""
    min_length = min(len(s) for s in strings)

    for i in range(min_length):
        char = strings[0][i]
        if all(s[i] == char for s in strings):
            prefix += char
        else:
            break

    print("The longest common prefix is:", prefix)