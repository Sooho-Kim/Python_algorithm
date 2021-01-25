#5355.py 화성수학
case=int(input())
for c in range(case):
    mars = list(map(str, input().split()))
    for i in range(len(mars)):
        if i==0:
            Sum=float(mars[i])
        else:
            if mars[i] == "@":
                Sum*=3
            if mars[i] == "%":
                Sum+=5
            if mars[i] == "#":
                Sum-=7
    print("%0.2f" %Sum)


