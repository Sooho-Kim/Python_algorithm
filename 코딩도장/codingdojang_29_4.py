x,y =map(int, input().split())

def calc(x, y):
    return x+y, x-y, x*y, x/y
a, s, m, d = calc(x, y)
print(a, s, m, d)