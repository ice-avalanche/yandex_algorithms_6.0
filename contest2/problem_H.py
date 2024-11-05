n = int(input())
s = input()
total = sum(int(count) for count in s.split())
half = (total + 1) // 2

cum_sum, median_i = 0, -1
for i, count_s in enumerate(s.split()):
    cum_sum += int(count_s)
    if cum_sum >= half:
        median_i = i
        break

print(sum(abs(i - median_i) * int(count) for i, count in enumerate(s.split())))
