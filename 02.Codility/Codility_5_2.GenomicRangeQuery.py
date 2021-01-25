# Task Score : 62, Correctness : 100, Performance : 0, 시간복잡도 N*M
# def solution(S,P,Q):
#     result = []
#     min_num = 5
#     for i in range(len(P)):
#         for j in range(P[i],Q[i]+1):
#             if S[j] == 'A':
#                 num = 1
#             if S[j] == 'C':
#                 num = 2
#             if S[j] == 'G':
#                 num = 3
#             if S[j] == 'T':
#                 num = 4
#             if num < min_num:
#                 min_num = num
#         result.append(min_num)
#         min_num = 5
#     return result

#Task Score : 100, Correctness : 100, Performance : 100
def solution(S, P, Q):
    R = []
    for i in range(len(P)):
        A = P[i]
        B = Q[i]
        min_num = 5
        if 'A' in S[A:B+1]:
            num = 1
        elif 'C' in S[A:B+1]:
            num = 2
        elif 'G' in S[A:B+1]:
            num = 3
        elif 'T' in S[A:B+1]:
            num = 4
        if min_num > num :
            min_num = num
        R.append(min_num)
    return R

S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]
T= solution(S,P,Q)
print(T)
