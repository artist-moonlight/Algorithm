while True:
    a= input()
    if a==".":
        break

    stack = []
    state = 1
    for i in a:
        if i=='(' or i=='[':
            stack.append(i)

        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                state = 0
                break

        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                state = 0
                break

    print("yes" if state and not(stack) else "no")
