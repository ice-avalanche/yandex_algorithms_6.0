n = int(input())
a = list(map(int, input().split()))
stack, result = [], [-1] * len(a)

for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1]
    stack.append(i)

print(*result)
