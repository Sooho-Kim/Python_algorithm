# 10886번 0=not cute / 1= cute
n = int(input())
count = 0
for i in range(n):
    a=int(input())
    count +=a
if count > int(n/2):
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
