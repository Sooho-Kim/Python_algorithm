#7567 그릇
bowl = input()
result =10
for i in range(1,len(bowl)):
    if bowl[i-1]=='(' and bowl[i] =='(':
        result +=5
    elif bowl[i-1]=='(' and bowl[i] ==')':
        result +=10
    elif bowl[i-1]==')' and bowl[i] =='(':
        result +=10
    elif bowl[i-1]==')' and bowl[i] ==')':
        result +=5
print(result)


