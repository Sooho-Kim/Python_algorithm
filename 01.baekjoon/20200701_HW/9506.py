#9506 약수들의 합
while True :
    n = int(input())
    if n == -1 :
        break
    number_list =[]
    i=1
    sum=0
    while i<n:
        if n%i ==0:
            number_list.append(i)
            sum += i
            i+=1
        elif n%i !=0 :
            i+=1
    if sum == n :
        print(n, end=' ')
        print('=', end=' ')
        for i in range(len(number_list)):
            if i != 0:
                print('+', end=' ')
            print(number_list[i], end= ' ')
    else :
        print(n, "is NOT perfect.")

