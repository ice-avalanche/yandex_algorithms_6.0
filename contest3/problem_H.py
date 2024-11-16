n = int(input())
stack = []
sums = [0]

for i in range(n):
    el = input()
    if el[0] == "+":
        stack.append(int(el[1:]))
        sums.append(sums[-1] + int(el[1:]))
    elif el[0] == "-":
        sums.pop()
        print(stack.pop())
    elif el[0] == "?":
        k = int(el[1:])
        print(sums[-1] - sums[-k-1])
