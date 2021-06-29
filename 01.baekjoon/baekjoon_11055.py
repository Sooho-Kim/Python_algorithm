from copy import deepcopy
N = int(input())
numbers = list(map(int, input().split()))
dp = deepcopy(numbers)
for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])
print(max(dp))
