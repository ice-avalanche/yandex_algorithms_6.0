n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pr = list(map(int, input().split()))

interest = sorted(range(n), key=lambda i: (-a[i], -b[i], i))
useful = sorted(range(n), key=lambda i: (-b[i], -a[i], i))

res = []
arr = set()
interest_i, useful_i = 0, 0

for p in pr:
    if p == 1:
        while useful_i < n:
            idx = useful[useful_i]
            if idx + 1 not in arr:
                res.append(idx + 1)
                arr.add(idx + 1)
                break
            useful_i += 1
    else:
        while interest_i < n:
            idx = interest[interest_i]
            if idx + 1 not in arr:
                res.append(idx + 1)
                arr.add(idx + 1)
                break
            interest_i += 1

print(' '.join(map(str, res)))
