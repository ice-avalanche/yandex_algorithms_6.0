n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))

i, j, res, n = 0, 0, 1, len(arr)

for j in range(len(arr)):
    while arr[j] - arr[i] > k:
        i += 1
    res = max(res, j - i + 1)

print(res)
