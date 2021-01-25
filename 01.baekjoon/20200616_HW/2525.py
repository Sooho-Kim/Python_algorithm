#4 오븐 시계
# from datetime import datetime
# today = datetime.today()
# print(today.hour, today.minute)
# n = input("조리시간을 입력하세요(분) >")
today_hour, today_minute = input().split()
n = input()
h = int(n)//60
n = int(n)%60
minute = (int(today_minute)+n)%60
minute_h = (int(today_minute)+n)//60
hour = int(today_hour)+minute_h+h
re_hour = hour % 24
re_minute = minute
print(re_hour, re_minute)