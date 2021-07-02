import sys
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[0]*N for _ in range(N)]
graph2 = [[0]*N for _ in range(N)]
for j in range(N):
    color = input()
    for idx, i in enumerate(color):
        if i == 'R':
            graph[j][idx] = 1
            graph2[j][idx] = 1
        elif i == 'B':
            graph[j][idx] = 2
            graph2[j][idx] = 2
        else:
            graph[j][idx] = 3
            graph2[j][idx] = 1

def dfs(graph, y, x, value):
    graph[y][x] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for idx in range(4):
        x0 = x + dx[idx]
        y0 = y + dy[idx]
        if (0 <= x0 < N) and (0 <= y0 < N) and (graph[y0][x0] == value):
            dfs(graph, y0, x0, value)

count = 0
for j in range(N):
    for i in range(N):
        if graph[j][i] != 0:
            value = graph[j][i]
            dfs(graph, j, i, value)
            count += 1
count2 = 0
for j in range(N):
    for i in range(N):
        if graph2[j][i] != 0:
            value = graph2[j][i]
            dfs(graph2, j, i, value)
            count2 += 1
print(count, count2)
