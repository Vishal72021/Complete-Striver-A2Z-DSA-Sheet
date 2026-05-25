print("Enter two strings: ")
s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("The strings are not anagrams.")
else:
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    if sorted_s1 == sorted_s2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")