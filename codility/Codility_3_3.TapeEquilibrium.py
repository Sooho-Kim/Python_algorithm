def solution(A):
    sum_A = sum(A)
    result = []
    sum_Left = 0
    sum_Right = sum_A
    for i in range(len(A)-1):
        sum_Left +=A[i]
        sum_Right -=A[i]
        print(sum_Left, sum_Right)
        result.append(abs(sum_Left - sum_Right))
    return min(result)