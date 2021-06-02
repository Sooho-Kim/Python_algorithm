def dfs(x, y, matrix):
    # 방문한 위치 0으로 변경
    matrix[x][y] = 0
    # 상하 좌우 확인
    for i in range(4):
        x0 = x + dx[i]
        y0 = y + dy[i]
        if (0<= x0 < N) and (0<= y0 < N):
            if matrix[x0][y0] != 0:
                dfs(x0, y0, matrix)
# 런타임 오류 제거
import sys
sys.setrecursionlimit(10**6)

import copy
N = int(input())
matrix = []
max_number = 0
for i in range(N):
    temp = list(map(int, input().split()))
    number = max(temp)
    if max_number <= number:
        max_number = number 
    matrix.append(temp)
# 상하 좌우
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 1
for k in range(1, max_number+1):
    temp_matrix = copy.deepcopy(matrix)
    for i in range(N):
        for j in range(N):
            if temp_matrix[i][j] <= k:
                temp_matrix[i][j] = 0
    
    count = 0
    for x in range(N):
        for y in range(N):
            if temp_matrix[x][y] != 0:
                dfs(x, y, temp_matrix)
                count += 1

    answer = max(answer, count)
print(answer)
