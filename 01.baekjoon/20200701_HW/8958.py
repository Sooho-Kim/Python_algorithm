#8958 OX퀴즈
Case = int(input())
for i in range(Case):
    A = input()
    result =0
    for i in A:
        if i == 'O':
            add +=1
            result += add
        elif i == 'X' :
            add = 0
    print(result)