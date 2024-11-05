n = int(input())
a = list(map(int, input().split()))
m, k = map(int, input().split())
x = list(map(int, input().split()))

rep, ans = [], []
ans.append(1)
min_ = 1

for i in range(1, n):
    if a[i] >= a[i-1]:
        if a[i] == a[i-1]:
            rep.append(i+1)
        if len(rep) > k:
            if min_ < rep[-k-1]:
                min_ = rep[-k-1]
    else:
        min_ = i + 1
    ans.append(min_)

print(*[ans[i-1] for i in x])
