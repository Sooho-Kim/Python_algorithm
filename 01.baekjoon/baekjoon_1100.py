"""
백준 1100번 하얀칸, url : https://www.acmicpc.net/problem/1100
.F.F...F
F...F.F.
...F.F.F
F.F...F.
.F...F..
F...F.F.
.F.F.F.F
..FF..F.
"""
count_white = 0
for i in range(8):
    block_list = []
    if i % 2 == 0:
        block_list = input()
        for idx, k in enumerate(block_list):
            if idx % 2 == 0 and k == 'F':
                count_white += 1
    else:
        block_list = input()
        for idx, j in enumerate(block_list):
            if idx % 2 == 1 and j == 'F':
                count_white += 1
print(count_white)
