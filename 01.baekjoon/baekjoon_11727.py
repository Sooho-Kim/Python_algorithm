N = int(input())
dp = [0]*N
dp[0] = 1
if N == 1:
    print(dp[0])
    exit()
elif N == 2:
    dp[1] = 3
    print(dp[1])
    exit()
else:
    dp[1] = 3
    for i in range(2, N):
        dp[i] = (dp[i-1] + 2*dp[i-2]) % 10007
    print(dp[N-1])
