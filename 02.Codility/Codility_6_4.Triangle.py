def solution(A):
    A.sort() # A를 오름차순으로 정렬
    result = 0 # 삼각형을 만드는 것이 없다고 가정
    for i in range(len(A)-2): # 인접한 3개의 값이 삼각형을 이루는 지 확인
        if A[i]+A[i+1] > A[i+2]:
            if A[i]+A[i+2]> A[i+1]:
                if A[i+1]+A[i+2] > A[i+1]:
                    result = 1 # 삼각형이 있으면 0을 1로 변환
    return result