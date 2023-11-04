import itertools

def solution(numbers, target):
    answer = 0
    len_num = len(numbers)
    pool = '+-'
    pool_list = list(itertools.product(pool,repeat = len_num))
    for i in pool_list:
        var_target = 0
        # 아래 반복구문이 짧아진다.
        for j in range(len_num):
            if i[j] == '+':
                var_target += numbers[j]
            else:
                var_target -= numbers[j]
        if var_target == target:
            answer += 1
    return answer