import itertools

# 생각한 원리 : +, - 가 나올수 있는 모든 경우의 수를 꺼내서 대입으로 반복문을 짠다.

def solution(numbers, target):
    answer = 0
    len_num = len(numbers)
    # 아래가 +, - 를 이용해서 나올수 있는 모든 경우의 수를 구한것이다.
    pool = '+-'
    pool_list = list(itertools.product(pool,repeat = len_num))
    # 반복문으로 모든 경우의 수를 계산해서 target과 같은지 판단한다.
    for i in pool_list:
        var_target = 0
        for j in range(len_num):
            if i[j] == '+':
                var_target += numbers[j]
            else:
                var_target -= numbers[j]
        if var_target == target:
            answer += 1
    return answer
