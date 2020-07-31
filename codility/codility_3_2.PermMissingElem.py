# PermMissingElem

def solution(A):
    if len(A) ==0 :
        result =1
    elif len(A) ==1:
        if A[0] == 1:
            result = 2
        else :
            result = 1
    else:
        result = sum(range(1,len(A)+2)) - sum(A)
    return result