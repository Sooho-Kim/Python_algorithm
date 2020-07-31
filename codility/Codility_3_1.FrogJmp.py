# FrogJmp
def solution(X,Y,D):
    d = Y-X
    Q = d // D
    R = d % D
    if R ==0:
        result = Q
    elif R < D:
        result = Q+1
    return result
