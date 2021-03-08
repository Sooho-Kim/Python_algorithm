import itertools
answer_str = input()
answer = int(answer_str)
length = len(answer_str)
permutation_list = list(map(''.join, itertools.permutations(answer_str, length)))
int_list = list(map(int, permutation_list))
sort_list = sorted(int_list)
if max(sort_list) == answer:
    print(0)
else:
    for i in range(len(sort_list)):
        if sort_list[i] == answer:
            result = sort_list[i+1]
    print(result)
print(itertools.permutations(answer_str, length))