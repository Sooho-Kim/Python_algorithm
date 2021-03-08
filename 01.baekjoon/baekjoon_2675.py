#2675 문자열 반복
from random import *
case=int(input())
A = []
for i in range(0, case):
    R, ST = map(str, input().split())
    R =int(R)
    answer=""
    for k in range(0,len(ST)):
        for r in range(0,R):
            answer+=ST[k]
    A.append(answer)
    print(A[i])


