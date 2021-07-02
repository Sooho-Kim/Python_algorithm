N = int(input())
graph = [[0]*N for _ in range(N)]
for i in range(N):
    line = input()
    for j in range(N):
        if line[j] == '1':
            graph[i][j] = int(line[j])
            
def dfs(graph, y, x):
    global count
    graph[y][x] = 0
    count += 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0 , 1, -1]
    
    for i in range(4):
        x0 = x + dx[i]
        y0 = y + dy[i]
        if (0 <= x0 < N) and (0 <= y0 < N) and (graph[y0][x0] == 1):
            dfs(graph, y0, x0)
            
count_list = []
for i in range(N):
    for j in range(N):
        count = 0
        if graph[j][i] == 1:
            dfs(graph, j, i)
            count_list.append(count)
count_list.sort()
print(len(count_list))
for i in range(len(count_list)):
    print(count_list[i])
