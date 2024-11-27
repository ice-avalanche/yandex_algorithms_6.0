import sys
sys.setrecursionlimit(2000001)

def calc_depth(num, father):
    if len(g[num]) <= 1: depth[num] = 1
    for son in g[num]:
        if son != father:
            depth[num] = max(depth[num], calc_depth(son, num) + 1)
            top3depth[num].append((depth[son], son))
            top3depth[num].sort(reverse=True)
            top3depth[num] = top3depth[num][:3]
    return depth[num]

def calc_upper_path(num, father, outer_path, inner_path):
    upath[num] = max(inner_path, outer_path)
    for son in g[num]:
        if son != father:
            son_inner = inner_path + 1
            son_outer = outer_path
            for path_len, other_son in top3depth[num]:
                if son != other_son:
                    son_outer = max(outer_path, son_inner + path_len)
                    son_inner = max(inner_path + 1, path_len + 1)
                    break
            calc_upper_path(son, num, son_outer, son_inner)

def calc_in_subtree(num, father):
    ans = 0
    for son in g[num]:
        if son != father:
            son_ans, son_path = calc_in_subtree(son, num)
            ans = max(ans, son_ans)
            cnt_used, sum_depths = 0, 0
            for i in range(len(top3depth[num])):
                if cnt_used < 2 and top3depth[num][i][1] != son:
                    cnt_used += 1
                    sum_depths += top3depth[num][i][0]
            ans = max(ans, son_path * sum_depths)
    max_path = sum(top3depth[num][i][0] for i in range(min(2, len(top3depth[num]))))
    ans = max(ans, (upath[num] - 1) * max_path)
    return ans, max_path

n = int(input())
g = [[] for _ in range(n+1)]
top3depth = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
depth = [-1] * (n + 1)
upath = [0] * (n + 1)
calc_depth(1, -1)
calc_upper_path(1, -1, 0, 0)
ans, _ = calc_in_subtree(1, -1)
print(ans)
