#Task : 56, Correctness : 100, Performance : 12
def solution(A):
    count = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if i+A[i]>=j-A[j]:
                count +=1
    if count > 10000000:
        count = -1
    return count

#100점짜리 참고한 알고리즘
#출처 : https://datacodingschool.tistory.com/33
def solution(A):
    arr = []
    for i, v in enumerate(A):
        arr.append((i-v, -1))
        arr.append((i+v, 1))

    arr.sort()
    intersection = 0
    intervals = 0

    for i,v in enumerate(arr):
        if v[1] == 1 :
            intervals -= 1
        if v[1] == -1:
            intersection += intervals
            intervals += 1
    if intersection > 10000000:
        intersection = -1

    return intersection

A=[1,5,2,1,4,0]
T=solution(A)
print(T)
