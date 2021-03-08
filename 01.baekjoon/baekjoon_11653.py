# 11653 소인수분해
n=int(input())
for i in range(2, int(n)+1):
    if n%i ==0 :
         a=n
         while a%i==0:
            print(i)
            a = a/i
            if a%i !=0:
                n=a
                break