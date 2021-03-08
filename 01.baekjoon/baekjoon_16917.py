import sys
A, B, C, x, y = map(int, sys.stdin.readline().split())
answer = []
answer.append(A*x + B*y)
answer.append(2*C*max(x, y))
answer.append(2*C*min(x, y) + (x-min(x, y))*A + (y-min(x, y))*B)
print(min(answer))

