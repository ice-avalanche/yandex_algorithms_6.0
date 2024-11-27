import sys
sys.setrecursionlimit(2000001)

def get_ans(num, is_root, father):
    global ans, bad
    if bad: return 0

    if is_root and len(g[num]) == 1 and len(g[g[num][0]]) > 1:
        get_ans(g[num][0], True, -1)
        return

    visited[num], cnt_big_childs, subtree_size = True, 0, 1
    for child in g[num]:
        if bad: return 0
        if visited[child] and child != father:
            bad = True; return 0
        elif not visited[child]:
            c_size = get_ans(child, False, num)
            subtree_size += c_size
            cnt_big_childs += c_size >= 2
            if (is_root and cnt_big_childs > 2) or (not is_root and cnt_big_childs > 1):
                bad = True; return 0

    cnt_small_childs = len(g[num]) - cnt_big_childs - 1 + is_root
    ans = (ans * factorial[cnt_small_childs]) % k
    if is_root:
        if cnt_small_childs == 0 and cnt_big_childs == 1:
            ans = (ans * len(g[g[num][0]])) % k
        ans = (ans * 2 * (1 + (cnt_small_childs > 0 and cnt_big_childs > 0 or cnt_big_childs == 2))) % k
    return subtree_size

n, m, k = map(int, input().split())

if m > n - 1:
    print(0)
else:
    factorial = [1] * (n + 1)
    for i in range(2, n + 1): factorial[i] = (factorial[i-1] * i) % k

    g, bad, ans, lonely, trees, visited = [[] for _ in range(n+1)], False, 1, 0, 0, [False] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b); g[b].append(a)

    for i in range(1, n + 1):
        if not visited[i] and g[i]:
            trees += 1
            get_ans(i, True, -1)
        if not g[i]: lonely += 1

    if bad:
        print(0)
    else:
        ans = (ans * factorial[trees]) % k
        for i in range(lonely):
            ans = (ans * (2 + n - lonely + i)) % k
        print(ans)
