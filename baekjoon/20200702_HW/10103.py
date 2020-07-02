#10103 주사위 게임
case = int(input())
result =[100, 100]
for i in range(case):
    n, m = map(int, input().split())
    if n > m :
        result[1] -= n
    elif n < m :
        result[0] -= m
    else :
        continue
for i in range(len(result)):
    print(result[i])
