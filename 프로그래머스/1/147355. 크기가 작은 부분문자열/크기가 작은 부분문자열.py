def solution(t, p):
    len_p = len(p)
    a = 0
    answer = 0
    num_list = []
    # print(len(t)-len_p)
    while a < len(t)-len_p+1:
        # print(a)
        num_list.append(t[a:a+len_p])
        a +=1
    # print(num_list)
    for i in num_list:
        if i <= p:
            answer += 1
    print(answer)
    # answer = 0
    return answer