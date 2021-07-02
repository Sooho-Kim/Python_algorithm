import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, matrix):
    global area
    area += 1
    # 방문한 위치 0으로 변경
    matrix[x][y] = 0
    # 상하 좌우 확인
    for i in range(4):
        x0 = x + dx[i]
        y0 = y + dy[i]
        if (0<= x0 < M) and (0<= y0 < N):
            if matrix[x0][y0] != 0:
                dfs(x0, y0, matrix)

# 영역 총 크기 받아서 map 할당
M, N, K = map(int, input().split())
Map = [[1] * N for _ in range(M)]

# 사각형 영역에 대해 0으로 변환
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for k in range(x1, x2): # [0, 1, 2]
        for j in range(y1, y2): # [4, 4]
            Map[j][k] = 0

# 상하좌우 좌표
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# 전체영역을 돌면서 영역의 크기 저장
whole_area = []
for i in range(M):
    for j in range(N):
        area = 0
        if Map[i][j] != 0:
            dfs(i, j, Map)
            whole_area.append(area)
            
whole_area.sort()       

# 구분된 영역의 수
print(len(whole_area))

#구분된 영역을 오름차순으로 출력
print(*whole_area)

# ver2
import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
graph = [[1] * N for _ in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(M-y1-1, M-y2-1, -1):
        for k in range(x1, x2):
            graph[j][k] = 0

def dfs(graph, y, x):
    global count
    count += 1
    graph[y][x] = 0

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        x0 = x + dx[i]
        y0 = y + dy[i]
        if (0<= y0 < M) and (0<= x0 < N):
            if graph[y0][x0] != 0:
                dfs(graph, y0, x0)
area_list = []
for y in range(M):
    for x in range(N):
        count = 0
        if graph[y][x] != 0:
            dfs(graph, y, x)
            area_list.append(count)
print(len(area_list))
area_list.sort()
print(*area_list)

