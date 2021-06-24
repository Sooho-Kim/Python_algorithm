N = int(input())
count = 0
number_list = [N]
visited_list = [0]*(N)
temp_list = []

def visited_check(N):
    visited_list[N] = 1
    temp_list.append(N)

while 1 not in number_list:
    count += 1
    temp_list = []
    for i in number_list:
        if i % 3 == 0:
            N1 = int(i/3)
            if visited_list[N1] != 1:
                visited_check(N1)
        if i % 2 == 0:
            N2 = int(i/2)
            if visited_list[N2] != 1:
                visited_check(N2)
        if i:
            N3 = i-1
            if visited_list[N3] != 1:
                visited_check(N3)           
    number_list = temp_list
print(count)

# ver2
from collections import deque

N = int(input())
count = 0
number_list = deque([N])
visited_list = [-1]*(N+1)
visited_list[N] = 0

while visited_list[1] == -1:
    i = number_list.popleft()
    count = visited_list[i]
    count += 1
    if i % 3 == 0:
        N1 = int(i/3)
        if visited_list[N1] == -1:
            visited_list[N1] = count
            number_list.append(N1)
    if i % 2 == 0:
        N2 = int(i/2)
        if visited_list[N2] == -1:
            visited_list[N2] = count
            number_list.append(N2)
    if i:
        N3 = i-1
        if visited_list[N3] == -1:
            visited_list[N3] = count
            number_list.append(N3)
print(visited_list[1])

