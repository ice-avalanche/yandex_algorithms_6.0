import sys
sys.setrecursionlimit(100000)

fin = open('input.txt', 'r')
n = int(fin.readline())
parents = {}
for i in range(n-1):
	child, parent = fin.readline().strip().split()
	parents[child] = parent
for line in fin:
	name1, name2 = line.strip().split()
	ancestors = {name1}
	while name1 in parents:
		name1 = parents[name1]
		ancestors.add(name1)
	while name2 not in ancestors:
		name2 = parents[name2]
	print(name2)
fin.close()
