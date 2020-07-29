def solution(N):
    count = 0
    max = 0
    binary_num = bin(N).lstrip('0b')
    for i in binary_num:
        if i == '1':
            if max < count:
                max = count
            count = 0
        else :
            count +=1
    return max
N = 1041
T = solution(N)
print(T)