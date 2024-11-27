import sys
sys.setrecursionlimit(200001)

def cnt_money(num):
    size = 1
    for child in childs[num]:
        c_money, c_size = cnt_money(child)
        ans[num] += c_money + c_size
        size += c_size
    ans[num] += 1
    return ans[num], size

n = int(input())
bosses = list(map(int, input().split()))
childs = [[] for _ in range(n)]
ans = [0] * n

for i, boss in enumerate(bosses, 1):
    childs[boss - 1].append(i)

cnt_money(0)
print(*ans)
