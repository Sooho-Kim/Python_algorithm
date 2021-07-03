import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())
channel = [0]*(M+1)
visited = [0]*(M+1)
for i in range(N):
    prefer, hate = map(int, input().split())
    if channel[hate] == 0:
        channel[hate] = prefer

stack = []
stack.append(P)
count = 0
result = 0
while stack:
    n = stack.pop()
    if (visited[n] == 0) and (channel[n] != 0): 
        visited[n] = 1
        stack.append(channel[n])
        count += 1
    elif visited[n] == 1:
        result = -1
        print(result)
        exit()
if result != -1:
    print(count)
