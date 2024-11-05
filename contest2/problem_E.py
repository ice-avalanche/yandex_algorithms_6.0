n = int(input())
arr = sorted(list(map(int, input().split())))

medians = []
left, right = 0, len(arr) - 1

while left <= right:
    current_len = right - left + 1
    if current_len % 2 == 1:
        median_index = (left + right) // 2
    else:
        median_index = (left + right) // 2

    medians.append(arr[median_index])
    arr.pop(median_index)
    right -= 1

print(*medians)
