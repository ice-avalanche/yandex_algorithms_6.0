def right(s):
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for c in s:
        if c in "{[(":
            stack.append(c)
        elif stack and c == pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0

s = input()
print("yes" if right(s) else "no")
