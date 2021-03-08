#10162 전자레인지
n = int(input())
time=[300, 60, 10]
count_list=[]
count=0
for i in time:
    while n >= i:
        n -= i
        count +=1
    count_list.append(count)
    count=0
if n != 0:
    print(-1)
else:
    print(count_list[0], count_list[1], count_list[2])