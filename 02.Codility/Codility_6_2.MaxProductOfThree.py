#Task : 100, Correctness : 100, Performance : 100 시간복잡도 : N*logN
def solution(A):
    count_un = 0
    count_up = 0
    under_A = []
    upper_A = []
    if len(A) == 3:
        Result = A[0]*A[1]*A[2]
    else :
        for i in A:
            if i <= 0:
                under_A.append(i)
                count_un +=1
            else :
                upper_A.append(i)
                count_up +=1
        under_A.sort()
        upper_A.sort()
        A.sort()
        if count_un <=1 or count_un == len(A):
            Result = A[-1]*A[-2]*A[-3]
        else :
            if count_up <=2:
                contain_negative = under_A[0] * under_A[1] * upper_A[-1]
                Result = contain_negative
            else :
                contain_postive = upper_A[-1]*upper_A[-2]*upper_A[-3]
                contain_negative = under_A[0]*under_A[1]*upper_A[-1]
                if contain_negative > contain_postive:
                    Result = contain_negative
                else :
                    Result = contain_postive
    return Result

A = [-3, 1, 2, -2, 5, 6]
T=solution(A)
print(T)