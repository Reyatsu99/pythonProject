def isValid( s: str):
    stack = []
    top = 0
    for i in s:
        if not stack :
            stack.append(i)
            top += 1
        else :
            if stack[-1] == i:
                stack.pop()
                top -= 1
        print(i)
    print(stack)
    return stack == []

print(isValid("()[]{}"))

