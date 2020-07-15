file = open('words.txt','r')
lines = file.readlines()
result = []
for i in lines :
    i = i.strip('\n')
    result.append(i)
    if i == i[::-1]:
        print(i)