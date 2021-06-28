N, K = map(int, input().split())
dp = [10001]*(K+5)
dp[0] = 0
coin_list = []
for _ in range(N):
    coin = int(input())
    coin_list.append(coin)
coin_list = list(set(coin_list))
coin_list.sort()
for coin in coin_list:
    for i in range(coin, K+1):
        if dp[i-coin] != 10001:
            dp[i] = min(dp[i], dp[i-coin] + 1)
if dp[K] != 10001:
    print(dp[K])
else:
    print(-1)
