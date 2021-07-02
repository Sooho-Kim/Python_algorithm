import sys 
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[0]*N for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if (graph[i][k] == 1) and (graph[k][j] == 1):
                graph[i][j] = 1
for i in graph:
    print(*i)
