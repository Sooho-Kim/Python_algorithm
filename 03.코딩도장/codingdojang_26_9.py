file = open('hello.txt','r')
result = []
for line in file :
    result = line.split()

for word in result :
    word = word.strip(",.")
    if 'c' in word :
        print(word)