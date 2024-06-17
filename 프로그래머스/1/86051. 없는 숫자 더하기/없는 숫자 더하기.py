def solution(numbers):
    var_list = []
    for i in range(10):
        if i not in numbers:
            var_list.append(i)
    # print(var_list)
    answer = 0
    for i in var_list:
        answer += i
    return answer