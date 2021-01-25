# 5086 배수와 약수
while True:
    a,b = map(int, input().split())
    if a !=0 and b!= 0 :
        if a>b and a%b ==0 :
            print("multiple")
        elif a<b and b%a ==0 :
            print("factor")
        elif a % b != 0:
            print("neither")
    else :
        break
