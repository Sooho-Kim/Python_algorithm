#Task Score : 60, Correctness : 100, Performance : 20
# def solution(A):
#     min_Slice = 10000
#     for i in range(len(A) - 1):
#         sum_Slice = A[i]
#         for j in range(i + 1, len(A)):
#             sum_Slice += A[j]
#             average_Slice = sum_Slice/(j-i+1)
#             if min_Slice > average_Slice:
#                 result = i
#                 min_Slice = average_Slice
#     return result

#task : 100, 시간복잡도 : N
# def solution(A):
#     minAvg = (A[0]+A[1])/2
#     result = 0
#     for i in range(2, len(A)):
#         avg = (A[i-2]+A[i-1]+A[i])/3
#         if minAvg > avg :
#             minAvg = avg
#             result = i-2
#         avg = (A[i-1]+A[i])/2
#         if minAvg > avg :
#             minAvg = avg
#             result = i-1
#     return result

#task : 100, 시간복잡도 : N
def solution(A):
    minAvg = (A[0]+A[1])/2
    result = 0
    for i in range(0, len(A)-1):
        avg = (A[i]+A[i+1])/2
        if minAvg > avg :
            minAvg = avg
            result = i

    for j in range(0, len(A)-2):
        avg = (A[j]+A[j+1]+A[j+2])/3
        if minAvg > avg :
            minAvg = avg
            result = j
    return result