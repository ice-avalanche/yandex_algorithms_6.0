n = int(input())
w = input()
s = input()

stack, ans, left = [], [], n

for i in range(n):
    if i < len(s):
        stack.append(s[i]) if s[i] in '([' else stack.pop()
    else:
        if not stack:
            ans.append(w[min(w.index('('), w.index('['))])
            stack.append(ans[-1])
        elif left == len(stack):
            ans.append(')' if stack.pop() == '(' else ']')
        elif left - len(stack) >= 2:
            top = stack[-1]
            next_char = w[min(w.index(')'), w.index('['), w.index('('))] if top == '(' else \
                        w[min(w.index(']'), w.index('['), w.index('('))]
            ans.append(next_char)
            stack.pop() if next_char in ')]' else stack.append(next_char)
    left -= 1

print(s + "".join(ans))
