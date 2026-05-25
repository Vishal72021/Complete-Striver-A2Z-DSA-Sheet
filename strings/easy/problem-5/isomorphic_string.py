print("Enter two strings: ")
s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("The strings are not isomorphic.")
else:
    mapping = {}
    reverse_mapping = {}

    for char1, char2 in zip(s1, s2):
        if char1 in mapping:
            if mapping[char1] != char2:
                print("The strings are not isomorphic.")
                break
        else:
            if char2 in reverse_mapping:
                print("The strings are not isomorphic.")
                break
            mapping[char1] = char2
            reverse_mapping[char2] = char1
    else:
        print("The strings are isomorphic.")