n, r = map(int, input().split())
d = list(map(int, input().split()))

count, left, right = 0, 0, 1
while right < len(d):
    count += (len(d) - right) * (d[right] - d[left] > r)
    left += (d[right] - d[left] > r)
    right += (d[right] - d[left] <= r)
print(count)
