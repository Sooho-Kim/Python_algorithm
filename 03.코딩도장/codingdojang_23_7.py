#지뢰찾기 바탕 만들기
n , m = map(int, input().split())
matrix =[]
for i in range(n):
    matrix.append(list(input()))
    for j in range(m):
        if matrix[i][j] =='.':
            matrix[i][j] = 0
axis = []
for k in range(n):
    if k==0 :
        min_y_axis = 0
        max_y_axis = k+1
    elif k == n-1:
        min_y_axis = k-1
        max_y_axis = k
    elif 0 < k < n-1:
        min_y_axis = k-1
        max_y_axis = k+1
    for l in range(m):
        if l == 0:
            min_x_axis = 0
            max_x_axis = l + 1
        if l == m-1:
            min_x_axis = l - 1
            max_x_axis = l
        if 0 < l < m-1:
            min_x_axis = l - 1
            max_x_axis = l + 1
        axis.append([min_x_axis, max_x_axis, min_y_axis, max_y_axis])
print(axis)
q=0
for o in range(n):
    for p in range(m):
        print(matrix)
        print('-----')
        q +=1
        a, b, c, d = axis[q-1]
        print(a,b,c,d)
        print('------')
        if matrix[o][p] =='*':
            for i in range(c,d+1):
                for j in range(a,b+1):
                    if matrix[i][j] == matrix[o][p]:
                        continue
                    elif matrix[i][j] == '*':
                        continue
                    elif matrix[i][j] is not '*':
                        matrix[i][j] +=1

for x in matrix:
    for i in x:
        print(i, end=' ')
    print()
