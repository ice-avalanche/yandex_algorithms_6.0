import sys
sys.setrecursionlimit(2000001)
INF = 10**9 + 1

def cnt_cost(num, parent):
	if len(g[num]) == 1 and parent != -1:
		marked[num], unmarked[num] = a[num], 0
		return
	nowcost = 0
	for child in g[num]:
		if child != parent:
			cnt_cost(child, num)
			nowcost += marked[child]
	unmarked[num] = nowcost
	nowcost = 0
	for child in g[num]:
		if child != parent:
			nowcost += min(marked[child], unmarked[child])
	marked[num] = nowcost + a[num]

def restore_ans(num, parent, is_mark):
	if is_mark:
		ans.append(num)
		for child in g[num]:
			if child != parent:
				restore_ans(child, num, marked[child] < unmarked[child])
	else:
		for child in g[num]:
			if child != parent:
				restore_ans(child, num, True)

n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
	u, v = map(int, input().split())
	g[u].append(v)
	g[v].append(u)
a = [0] + list(map(int, input().split()))
marked = [INF] * (n + 1)
unmarked = [INF] * (n + 1)
cnt_cost(1, -1)
if n == 1:
	unmarked[1] = INF
ans = []
restore_ans(1, -1, marked[1] < unmarked[1])
print(min(marked[1], unmarked[1]), len(ans))
print(*ans)
