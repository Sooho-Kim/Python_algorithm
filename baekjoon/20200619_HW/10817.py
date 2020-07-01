#10817 세 수
#방법1
A, B, C = map(int, input().split())
if A > B :
    if B > C:
        print(B)
    elif C > B :
        if A > C :
            print(C)
        else :
            print(A)
    elif B == C:
        print(B)
elif B > A :
    if A > C:
        print(A)
    elif C > A :
        if B > C :
            print(C)
        else :
            print(B)
    elif A == C:
        print(A)
elif A == B :
    print(B)

#방법2
numbers = [A, B, C]
numbers.sort(reverse=True)
print(numbers[1])