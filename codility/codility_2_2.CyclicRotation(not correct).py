def solution(A):
    if len(A) ==1:
        return A[0]
    A = sorted(A)
    if A[0] != A[1]:
        return A[0]
    if A[int((len(A)-1)/2)] != A[int((len(A)-1)/2)+1]:
        return A[int((len(A)-1)/2)]
    if A[len(A)-1] != A[len(A)-2]:
        return A[len(A)-1]
