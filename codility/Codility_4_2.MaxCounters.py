# #시간복잡도 N*M 66%
# def solution(N,A):
#     result = [0]*N
#     for i in range(len(A)):
#         if A[i] <= N:
#             result[A[i]-1] +=1
#         else :
#             M = max(result)
#             result = [M]*N
#     return result
#
# #시간복잡도 N*M 66%
# def solution(N,A):
#     result = [0]*N
#     for i in range(len(A)):
#         if A[i] <= N:
#             result[A[i]-1] +=1
#         else :
#             result.sort()
#             result = [result[-1]]*N
#     return result

#시간복잡도 N+M 100% - 참고하고 풀었음
def solution(N,A):
    result = [0]*N
    last_update = 0
    max_val = 0
    for i in range(len(A)):
        if A[i] <= N:
            if result[A[i]-1] < last_update:
                result[A[i]-1] = last_update
            result[A[i]-1] +=1
            if result[A[i]-1] >max_val:
                max_val = result[A[i]-1]
        else :
             last_update = max_val
    for i in range(len(result)):
        if result[i] < last_update:
            result[i] = last_update
    return result

N=5
A=[1,1,3,2,4,5,7,1]
T=solution(N,A)
print(T)