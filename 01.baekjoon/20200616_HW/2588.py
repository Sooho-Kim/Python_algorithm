#2588번 곱셈
A=input()
B=input()
for b in range(len(B)-1,-1, -1):
    print(b)
    C=int(A)*int(B[b])
    print(C)
    C=0

A=input()
B=input()
for b in range(0, len(B)):
    if b == 0:
        A3=int(A)*int(B[b])
    if b == 1:
        A2=int(A)*int(B[b])
    if b == 2:
        A1=int(A)*int(B[b])
print(A1)
print(A2)
print(A3)
print(A3*100+A2*10+A1)