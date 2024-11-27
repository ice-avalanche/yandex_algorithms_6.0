import sys
sys.setrecursionlimit(100000)

def cnt_desc(num):
	descendants[num] = 1
	for son in g[num]:
		if descendants[son] == -1:
			descendants[num] += cnt_desc(son)
	return descendants[num]

n = int(input())
g = []
descendants = [-1] * (n + 1)
for i in range(n+1):
	g.append([])
for i in range(n-1):
	a, b = map(int, input().split())
	g[a].append(b)
	g[b].append(a)
cnt_desc(1)
print(*descendants[1:])
