#1934 최소공배수
Case = int(input())
for i in range(Case) :
    A, B = map(int, input().split())
    result = 1
    if A > B :
        max_num = A
        min_num = B
    else :
        max_num = B
        min_num = A
    for i in range(2, int(max_num)+1):
        while max_num%i==0 and min_num%i==0:
            result *=i
            max_num = max_num//i
            min_num = min_num//i
    final_result = result*max_num*min_num
    print(final_result)
