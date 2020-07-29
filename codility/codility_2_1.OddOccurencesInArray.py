def solution(A, K):
    count =0
    temp = 0
    if len(A) == K or len(A)==0:
        return A
    elif len(A) != K and len(A)>0 :
        while count != K :
            temp = A[len(A)-1]
            for i in range(len(A)):
                if i != len(A)-1:
                    A[len(A)-1-i] = A[len(A)-i-2]
                else:
                    A[0] = temp
            count +=1
        return A