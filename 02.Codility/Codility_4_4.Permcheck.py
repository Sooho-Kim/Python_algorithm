#total:100
def solution(A):
    B = list(set(A)) # A의 중복제거 후 리스트로 변환
    if len(B) != len(A): # A의 크기 != B의 크기 (중복 포함되어 있다는 이야기)
        return 0
    B.sort() # B 순서대로 나열(오름차순)
    count = 1
    for i in B:
        if count == i:
            result =1
            count +=1
        else :
            result = 0
            break
    return result