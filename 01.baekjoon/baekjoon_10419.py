"""
백준 10419번 지각, url : https://www.acmicpc.net/problem/10419

"""
import sys
n = int(sys.stdin.readline())
for i in range(n):
    class_time = int(sys.stdin.readline())
    max_number = 0
    for j in range(1, class_time):
        if j+(j**2) <= class_time:
            max_number += 1
            continue
        else:
            break
    print(max_number)

