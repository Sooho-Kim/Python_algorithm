import sys
sys.setrecursionlimit(10**9)

T = int(input())

def dfs(graph, y, x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[y][x] = 0

    for i in range(4):
        x0 = x + dx[i]
        y0 = y + dy[i]
        if (0 <= x0 < M) and (0 <= y0 < N) and (graph[y0][x0] == 1):
            graph[y0][x0] = 0
            dfs(graph, y0, x0)

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*(M) for _ in range(N)]
    count = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if (graph[i][j] == 1):
                dfs(graph, i, j)
                count += 1
    print(count)
