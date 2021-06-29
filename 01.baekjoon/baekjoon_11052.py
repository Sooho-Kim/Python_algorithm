N = int(input())
cost_list = list(map(int, input().split()))

dp = [[0]*(N+1) for i in range(N+1)]

for idx, i in enumerate(cost_list):
    for j in range(N):
        if j < idx:
            dp[idx+1][j+1] = dp[idx][j+1]
        else:
            dp[idx+1][j+1] = max(dp[idx][j+1], dp[idx][j-idx]+i, dp[idx+1][j-idx]+i)
print(dp[N][-1])
