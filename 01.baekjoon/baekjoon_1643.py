N = int(input())
count = 0
number_list = [N]
while 1 not in number_list:
    count += 1
    temp_list = []
    for i in number_list:
        if i % 3 == 0:
            N1 = int(i/3)
            temp_list.append(N1)
        if i % 2 == 0:
            N2 = int(i/2)
            temp_list.append(N2)
        if i:
            N3 = i-1
            temp_list.append(N3)
    number_list = set(temp_list)
print(count)
