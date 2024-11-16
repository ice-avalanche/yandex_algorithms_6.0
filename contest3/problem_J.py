from collections import deque

def sol():
    hw = sorted((h[i], w[i]) for i in range(n))
    if any(hw[i][1] >= vasya for i in range(n)):
        return 0

    ans = hw[-1][0] - hw[0][0]
    deq = deque()
    now_len, right = hw[0][1], 1

    for left in range(n - 1):
        while right < n and now_len < vasya:
            now_len += hw[right][1]
            while deq and deq[-1] < hw[right][0] - hw[right - 1][0]:
                deq.pop()
            deq.append(hw[right][0] - hw[right - 1][0])
            right += 1
        if now_len >= vasya:
            ans = min(ans, deq[0])
        now_len -= hw[left][1]
        if deq and deq[0] == hw[left + 1][0] - hw[left][0]:
            deq.popleft()

    return ans

n, vasya = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))
print(sol())
