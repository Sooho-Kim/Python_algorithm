def prime_number_generator(start, stop):
    if start == 1:
        yield start
        start +=1
    while start < stop and start >1:
        n=1
        for i in range(2, start):
            if start%i !=0:
                n +=1
            else :
                continue
        if start-1 == n:
            yield start
        start += 1


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')