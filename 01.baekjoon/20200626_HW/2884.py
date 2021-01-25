#2884 알람 시계
Hour, Minute = map(int, input().split())
if Minute >= 45 :
    Minute -= 45
elif Minute < 45 :
    Minute += 15
    if Hour == 0 :
        Hour = 24
    Hour -=1
print(Hour, Minute)
