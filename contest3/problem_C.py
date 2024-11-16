import collections

n, k = map(int, input().split())
nums = list(map(int, input().split()))

d = collections.deque()
out = []
for i, n in enumerate(nums):
    while d and nums[d[-1]] > n:
        d.pop()
    d.append(i)
    if d[0] == i - k:
        d.popleft()
    if i>=k-1:
        print(nums[d[0]])
