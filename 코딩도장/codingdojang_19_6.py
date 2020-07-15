n = int(input())
for i in range(n):
    for j in range(2*n-1):
        if j <= n-1 + i and n-1 - i <= j :
            print("*", end="")
        else :
            print(" ", end="")
    print()