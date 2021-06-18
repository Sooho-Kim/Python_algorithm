N = int(input())
dp = [0]*(N)
if N == 1:
    print(3)
elif N == 2:
    print(7)
else:
    dp[0] = 3
    dp[1] = 7
    for i in range(2, N):
        dp[i] = (2*dp[i-1] + dp[i-2])%9901
    print(dp[N-1])
