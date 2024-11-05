n, c = map(int, input().split())
s = input()

left = count_a = count_b = rude = max_len = 0

for right in range(n):
    count_a += s[right] == 'a'
    if s[right] == 'b':
        count_b += 1
        rude += count_a
    while rude > c:
        rude -= count_b * (s[left] == 'a')
        count_a -= s[left] == 'a'
        count_b -= s[left] == 'b'
        left += 1
    max_len = max(max_len, right - left + 1)
    
print(max_len)
