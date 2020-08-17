#Task : 50, correctness : 100, performance : 0, 시간복잡도 : N**2
# def solution(A):
#     count = 0
#     for i in range(len(A)):
#         if A[i] == 0 :
#             for j in range(i,len(A)):
#                 if A[j] == 1:
#                     count +=1
#     if count > 1000000000:
#         count = -1
#     return count

#Task : 100, correctness : 100, performace : 100, 시간복잡도 : N
def solution(A):
    Sum = 0
    basket = [0]*2 # basket[0] : 0의 갯수, basket[1] : 1의 갯수(0과 0사이)
    for i in A:
        if i == 0 :
            basket[0] +=1
            basket[1] = 0
        elif i == 1 :
            basket[1] =1
            Sum += basket[0] * basket[1]
    if Sum > 1000000000:
        Sum = -1
    return Sum