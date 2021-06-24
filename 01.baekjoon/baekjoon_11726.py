N = int(input())
dp = [0]*N
for i in range(N):
    if i <= 1:
        dp[i] = i+1
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[N-1])
