n = int(input())
a, b = map(int, input().split())
a, b = a - 1, b - 1
qs = [[] for _ in range(4)]

for i in range(n):
    d, t = map(int, input().split())
    qs[d - 1].append((t, i))

for q in qs:
    q.sort()

ans, time = [0] * n, 1

while n > 0:
    moves = [False] * 4
    for dir in range(4):
        if qs[dir] and qs[dir][0][0] <= time:
            right = (dir - 1) % 4
            if (dir in {a, b}) and (right in {a, b}) and qs[right] and qs[right][0][0] <= time:
                continue
            if dir not in {a, b} and (
                (qs[right] and qs[right][0][0] <= time) or
                (qs[a] and qs[a][0][0] <= time) or
                (qs[b] and qs[b][0][0] <= time)
            ):
                continue
            moves[dir] = True

    for dir in range(4):
        if moves[dir]:
            t, idx = qs[dir].pop(0)
            ans[idx] = time
            n -= 1

    time += 1

print(*ans, sep='\n')
