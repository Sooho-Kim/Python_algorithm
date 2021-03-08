# n = input()
# m = input()
# count = 0
# for i in range(0,len(n)-(len(m)-1), len(m)):
#     if m == n[i:i+(len(m))]:
#         count += 1
# print(count)
n = input()
m = input()
count = 0
i = 0
while i <len(n)-(len(m)-1):
    if m == n[i:i+(len(m))]:
        i += len(m)
        count += 1
    else :
        i += 1
print(count)