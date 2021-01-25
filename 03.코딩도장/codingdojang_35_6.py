class Time:
    def __init__(self, hour, minute, second): #속성값 정의
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod #클래스 속성, 클래스 메서드에 접근해야 할 때 사용
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time

    @staticmethod #외부 상태에 영향을 끼치지 않는 함수 (인스턴스의 상태를 변화시키지 않음)
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <=23 and minute <=59 and second <=59

time_string = input()
#아래에서 사용된 method는 is_time_valid, from_string
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')