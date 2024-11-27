import sys
sys.setrecursionlimit(2000001)
MOD = 10**9 + 7

def count_topsorts(num, parent):
    d1 = [1]
    for child, kind in g[num]:
        if child == parent:
            continue
        nd = count_topsorts(child, num)
        nds = [0] * (len(nd) + 1)
        for i in range(len(nd)):
            nds[i + 1] = (nds[i] + nd[i]) % MOD
        d2 = [0] * (len(d1) + len(nd))
        for x1, val1 in enumerate(d1):
            for cnt1 in range(len(nd) + 1):
                x2 = x1 + cnt1
                val = cnk[x2][cnt1] * cnk[len(d2) - 1 - x2][len(nd) - cnt1] * val1 % MOD
                val = val * (nds[cnt1] if kind == 1 else (nds[-1] - nds[cnt1])) % MOD
                d2[x2] = (d2[x2] + val) % MOD
        d1 = d2
    return d1

n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append((v, 0))
    g[v].append((u, 1))

cnk = [[1] + [0] * n for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, i + 1):
        cnk[i][j] = (cnk[i - 1][j - 1] + cnk[i - 1][j]) % MOD

print(sum(count_topsorts(1, -1)) % MOD)
