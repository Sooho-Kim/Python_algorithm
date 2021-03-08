# 3009 네번째 점
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
list_A = [Ax, Ay]
list_B = [Bx, By]
list_C = [Cx, Cy]
list_D = []
for i in range(len(list_A)):
    if list_A[i] == list_B[i] :
        list_D.append(list_C[i])
    elif list_A[i] == list_C[i] :
        list_D.append(list_B[i])
    elif list_B[i] == list_C[i] :
        list_D.append(list_A[i])
print(list_D[0], list_D[1])
