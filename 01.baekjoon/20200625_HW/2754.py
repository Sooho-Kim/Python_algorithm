#2754 학점계산
n = str(input())
if n == 'A+':
    result = 4.3
elif n == 'A0':
    result = 4.0
elif n == 'A-':
    result = 3.7
elif n == 'B+':
    result = 3.3
elif n == 'B0':
    result = 3.0
elif n == 'B-':
    result = 2.7
elif n == 'C+':
    result = 2.3
elif n == 'C0':
    result = 2.0
elif n == 'C-':
    result = 1.7
elif n == 'D+':
    result = 1.3
elif n == 'D0':
    result = 1.0
elif n == 'D-':
    result = 0.7
elif n == 'F':
    result = 0.0
print(result)
