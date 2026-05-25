print("Enter a string of parentheses: ")
s = input()

stack = []
result = ""

for char in s:
    if char == '(':
        if stack:
            result += char
        stack.append(char)
    else:
        stack.pop()
        if stack:
            result += char

print("String after removing outermost parentheses:", result)