cost = input()
cost = cost.rsplit(";")
cost_list = list(map(int, cost))
cost_list.sort(reverse = True)
for i in cost_list:
    print('{0:>9,}'.format(i))
