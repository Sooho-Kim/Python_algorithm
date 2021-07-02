import sys
sys.setrecursionlimit(10**9)

N, M, K = map(int, input().split())
graph = [[0]*(M+1) for _ in range(N+1)]
for _ in range(K):
    y, x = map(int, input().split())
    graph[y][x] = 1

def dfs(graph, x, y):
    global count
    count += 1
    graph[y][x] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        x0 = x + dx[i]
        y0 = y + dy[i]
        if (1 <= x0 <= M) and (1 <= y0 <= N) and (graph[y0][x0] == 1):
            graph[y0][x0] = 0
            dfs(graph, x0, y0)

count_list = []
for i in range(1, N+1):
    for j in range(1, M+1):
        count = 0
        if graph[i][j] == 1:
            dfs(graph, j, i)
            count_list.append(count)
print(max(count_list))
