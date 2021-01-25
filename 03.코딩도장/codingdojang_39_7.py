#표준 입력으로 정수 3개 입력, 첫번째: 시작하는 초, 두번째는 반복을 끝낼 초., 세번째는 인덱스

class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = -1

    def __getitem__(self, index):
        if index < self.stop-self.start:
            self.minute = (self.start+index)//60
            self.second = (self.start+index)%60
            if self.minute >59:
                self.hour = self.minute //60
                self.minute = self.minute % 60
                if self.hour > 23:
                    self.hour = self.hour % 24
            else:
                self.hour=0
            return '{0:>02d}:{1:>02d}:{2:>02d}'.format(self.hour, self.minute, self.second)
        else:
            raise IndexError

start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')