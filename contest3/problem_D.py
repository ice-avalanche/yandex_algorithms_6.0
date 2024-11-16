stack = []
for a in input().split():
    if a.isdigit():
        stack.append(int(a))
    else:
        op1, op2 = stack.pop(), stack.pop()
        stack.append(eval(f"{op2}{a}{op1}"))
print(stack.pop())
