n, b = map(int, input().split())
a = list(map(int, input().split()))

new = [0] * (n+1)

for i in range(0, n):
    new[i] += a[i]
    if new[i] > b:
        new[i+1] += new[i] - b

print(sum(new))
