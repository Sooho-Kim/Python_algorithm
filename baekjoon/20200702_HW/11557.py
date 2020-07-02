# 11557 Yangjojang of the year
T = int(input())
for i in range(T):
    N = int(input())
    school = []
    num = []
    for i in range(N):
        m, n = map(str, input().split())
        school.append(m)
        num.append(int(n))
    print(school[num.index(max(num))])
