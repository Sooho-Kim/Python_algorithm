# 10988번 팰린드롬인지 확인하기
word = input()
for i in range(0,int((len(word)+1)/2)):
    if word[i] ==word[-i-1]:
        a = 1
        if i == int((len(word)+1)/2):
            break
    else :
        a = 0
        break
print(a)