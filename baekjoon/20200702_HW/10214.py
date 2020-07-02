# 10214 baseball
case = int(input())
for i in range(case):
    Yonsei = 0
    Korea = 0
    for j in range(9):
        m, n = map(int, input().split())
        Yonsei += m
        Korea += n
    if Yonsei > Korea :
        print("Yonsei")
    elif Korea > Yonsei :
        print("Korea")
    else :
        print("Draw")