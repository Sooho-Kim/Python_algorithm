import sys
sys.setrecursionlimit(10**9)
from collections import deque

input = sys.stdin.readline

def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
#             # graph 변형으로 인해 문제 생김
#             while graph[n]:
#                 k = graph[n].pop()
            for k in graph[n][::-1]:
                if k in visited:
                    continue
                else:
                    stack.append(k)
    return visited

def bfs(graph, start):
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
#             # 이렇게 하면 안된다.
#             queue += set(graph[n]) -set(visited)
            queue += graph[n]
    return visited

n, m, start = map(int, input().split())
graph_list = []
for i in range(n+1):
    graph_list.append([])
for i in range(m):
    parent, child = map(int, input().split())
    graph_list[parent].append(child)
    graph_list[child].append(parent)
for idx, i in enumerate(graph_list):
    i = sorted(i)
    graph_list[idx] = i

#pop때문에 graph변형이 존재하는 문제있을 때, 어떻게 처리? -> pop을 변경해주기
dfs = dfs(graph_list, start)
bfs = bfs(graph_list, start)
print(*dfs) # ' '.join(map(str, dfs))
print(*bfs) # ' '.join(map(str, bfs))
