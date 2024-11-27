import sys
sys.setrecursionlimit(100000)

def add(tree, param):
	while tree and tree[0] != param:
		tree = tree[1] if param < tree[0] else tree[2]
	if not tree:
		tree += [param, [], []]
		return True
	return False

def search(tree, param):
	while tree and tree[0] != param:
		tree = tree[1] if param < tree[0] else tree[2]
	return bool(tree)

def print_tree(tree, depth):
	if tree:
		print_tree(tree[1], depth + 1)
		print('.' * depth + str(tree[0]))
		print_tree(tree[2], depth + 1)

with open('input.txt', 'r') as fin:
	tree = []
	for line in fin:
		line = line.strip()
		if line == 'PRINTTREE':
			print_tree(tree, 0)
		else:
			comm, param = line.split()
			param = int(param)
			if comm == 'ADD':
				print('DONE' if add(tree, param) else 'ALREADY')
			elif comm == 'SEARCH':
				print('YES' if search(tree, param) else 'NO')
