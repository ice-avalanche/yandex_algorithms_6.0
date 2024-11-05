N, K = map(int, input().split())
R = list(map(int, input().split()))

count, cur_sum, sum_dict = 0, 0, {0: 1}
for el in R:
    cur_sum += el
    count += sum_dict.get(cur_sum - K, 0)
    sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1

print(count)
