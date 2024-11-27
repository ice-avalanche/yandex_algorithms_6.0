import sys
sys.setrecursionlimit(100000)

def get_cnt(name):
	if cnt[name] == -1:
		cnt[name] = 0
		if name in childs:
			for child in childs[name]:
				cnt[name] += get_cnt(child) + 1
	return cnt[name]

n = int(input())
childs = {}
cnt = {}
for i in range(n-1):
	child, parent = input().split()
	if parent not in childs:
		childs[parent] = []
	childs[parent].append(child)
	cnt[child] = -1
	cnt[parent] = -1
for name in cnt:
	get_cnt(name)
for name in sorted(cnt.keys()):
	print(name, cnt[name])
