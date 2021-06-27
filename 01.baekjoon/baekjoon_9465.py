N = int(input()) # 테스트케이스
for _ in range(N):
    M = int(input())
    dp = [[0]*(M+1) for _ in range(2)]
    array = [[0]*(M+1) for _ in range(2)]
    for i in range(2):
        array[i][1:] = list(map(int, input().split()))
    for j in range(M+1):
        if j == 0:
            dp[0][j] = array[0][j]
            dp[1][j] = array[1][j]
        else:
            dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + array[0][j]
            dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + array[1][j]
    print(max(dp[0][M], dp[1][M]))
