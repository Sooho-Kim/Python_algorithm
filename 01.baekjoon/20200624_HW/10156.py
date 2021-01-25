# 10156 과자
cost, num, money = map(int, input().split())
if (cost*num)-money > 0 :
    result = (cost*num)-money
else :
    result = 0
print(result)



