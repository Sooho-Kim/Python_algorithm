# Task score : 54, Correctness : 100, performance : 0
# def solution(X,A):
#     count = 0
#     unique_list = []
#     sum_X = sum(range(1,X+1))
#     for index, value in enumerate(A):
#         if index == 0:
#             unique_list.append(value)
#             count += value
#             if count == sum_X:
#                 return index
#         elif index >= 1:
#             if value not in unique_list:
#                 unique_list.append(value)
#                 count += value
#                 if count == sum_X:
#                     return index
#         elif index == len(A):
#             if value not in unique_list:
#                 unique_list.append(value)
#                 count += value
#                 if count == sum_X:
#                     return index
#             elif value in unique_list and count != sum_X :
#                 return -1

# Task score : 54, Correctness : 100, performance : 0
# def solution(X,A):
#     sum_X=sum(range(1,X+1))
#     i=0
#     count =0
#     unique_list = []
#     while count < sum_X:
#         if 0<=i<len(A):
#             if A[i] not in unique_list:
#                 unique_list.append(A[i])
#                 count +=A[i]
#                 i +=1
#             else :
#                 i +=1
#         elif i == len(A):
#             if count != sum_X:
#                 return -1
#                 break
#     return i-1

# task score : 27, correctness :50, performance : 0
# def solution(X, A):
#     sum_X = sum(range(1,X+1))
#     sum_A = sum(set(A))
#     unique_list = []
#     unique_sum = 0
#     if sum_X == sum_A :
#         for index, value in enumerate(A):
#             if value not in unique_list:
#                 unique_list.append(value)
#                 unique_sum +=value
#                 if value == X and sum_X==unique_sum:
#                     return index
#     else :
#         return -1

def solution(X,A):
    unique_list = [0]*X
    sum_unique = 0
    for i in range(len(A)):
        if unique_list[A[i]-1] == 0:
            unique_list[A[i]-1]= 1
            sum_unique += 1
            if sum_unique == X:
                result = i
                print(unique_list)
            else :
                result = -1
        else :
            continue
    return result
#
# X = 5
# A = [1,2,1,2,1,2]
# print(solution(X,A))
