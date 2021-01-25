a = list(input().split())
count =0
for i in range(len(a)):
    a[i] = a[i].strip("',.")
    if a[i] == 'the':
        count +=1
print(count)