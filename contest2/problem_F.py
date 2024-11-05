n = int(input())
arr = sorted(map(int, input().split()))

suf_sum = [0] * (n + 1)
suf_prod_sum = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    suf_sum[i] = (suf_sum[i + 1] + arr[i]) % 1000000007
    suf_prod_sum[i] = (suf_prod_sum[i + 1] + arr[i] * suf_sum[i + 1]) % 1000000007

total_sum = 0
for i in range(n - 2):
    total_sum = (total_sum + arr[i] * suf_prod_sum[i + 1]) % 1000000007

print(total_sum)
