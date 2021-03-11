"""
백준 14648번 쿼리맛보기, url : https://www.acmicpc.net/problem/14648
"""
n, m = map(int, input().split())
number_list = list(map(int, input().split()))
for i in range(m):
    query = list(map(int, input().split()))
    if len(query) == 5:
        result = sum(number_list[query[1]-1:query[2]])-sum(number_list[query[3]-1:query[4]])
    else:
        result = sum(number_list[query[1]-1:query[2]])
        number_list[query[1]-1], number_list[query[2]-1] = number_list[query[2]-1], number_list[query[1]-1]
    print(result)


