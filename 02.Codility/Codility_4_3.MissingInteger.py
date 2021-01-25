#Task : 66, Correctness : 80, Performance : 50
# def solution(A):
#     A = list(set(A))
#     A.sort()
#     count = A[0]
#     if count > 1 :
#         return 1
#     for i in A :
#         if count == i:
#             count +=1
#             result = count
#         else :
#             result = count
#             break
#     if result <= 0:
#         result = 1
#     return result

#Task : 100, Correctness : 100, Performance : 100
def solution(A):
    A.sort()
    A = list(set(A))
    missingdata = 1
    for i in A :
        if i == missingdata :
            missingdata +=1
    return missingdata
