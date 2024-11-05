from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
print(*accumulate(a))
