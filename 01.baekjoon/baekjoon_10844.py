from copy import deepcopy 
N = int(input())
dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if N == 1:
    print(sum(dp))
else:
    for _ in range(N-1):
        temp_dp = deepcopy(dp)
        dp = [0]*10
        for idx, i in enumerate(temp_dp):
            if idx == 0:
                dp[idx+1] += i
            elif idx < 9:
                dp[idx-1] += i
                dp[idx+1] += i
            else:
                dp[idx-1] += i
    print(sum(dp)%1000000000)
