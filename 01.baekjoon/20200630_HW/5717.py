#5717번 상근이의 친구들
while True :
    Male, Female = map(int, input().split())
    if Male > 0 or Female > 0 :
        Friends = Male+Female
        print(Friends)
    else :
        break