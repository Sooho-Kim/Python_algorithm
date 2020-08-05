#Task : 50,  Correctness : 100, 시간복잡도 B-A
# def solution(A, B, K):
#     div = 1
#     count = 0
#     for i in range(A,B+1,div):
#         if i % K == 0:
#             count +=1
#             div = K
#     return count

#Task : 100, Correctness : 100, 시간복잡도 : 1
def solution(A, B, K):
    QA = A//K
    RA = A%K
    QB = B//K
    count = QB-QA
    if RA ==0:
        count +=1
    return count