#2476 주사위 게임
case = int(input())
total_result=[]
for i in range(case) :
    A, B, C = map(int, input().split())
    if A == B == C :
        same_num = A
        result = 10000+same_num*1000
    elif A == B or B == C or C == A :
        if A == B:
            same_num = A
            result = 1000 + same_num * 100
        if B == C :
            same_num = B
            result = 1000 + same_num * 100
        if C == A :
            same_num = C
            result = 1000 + same_num * 100
    else :
        same_num = max(A, B, C)
        result = same_num*100
    total_result.append(result)
print(max(total_result))
