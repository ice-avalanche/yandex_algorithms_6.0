import sys
sys.setrecursionlimit(100000)

def get_dist(name):
	if dist[name] == -1:
		dist[name] = get_dist(parents[name]) + 1 if name in parents else 0
	return dist[name]

n = int(input())
parents, dist = {}, {}
for _ in range(n - 1):
	child, parent = input().split()
	parents[child] = parent
	dist.setdefault(child, -1)
	dist.setdefault(parent, -1)

[get_dist(name) for name in dist]
[print(name, dist[name]) for name in sorted(dist)]
