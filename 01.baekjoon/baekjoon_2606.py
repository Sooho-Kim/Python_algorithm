from collections import deque
node = int(input())
connect = int(input())
graph_list = []
for i in range(node+1):
    graph_list.append([])
# 무조건 단방향이라는 조건이 없어서.. 양방향 고려하기!
for i in range(connect):
    parent, child = map(int, input().split(' '))
    graph_list[parent].append(child)
    graph_list[child].append(parent)

visited = []
queue = deque([1])

while queue:
    n = queue.popleft()
    if n not in visited:
        visited.append(n)
        queue += set(graph_list[n]) - set(visited)
print(len(visited)-1)
