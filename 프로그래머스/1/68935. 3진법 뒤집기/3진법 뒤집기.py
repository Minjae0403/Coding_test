def solution(n):
    n3_list=[]
    while n > 2:
        # print(n//3)
        # print(n%3)
        n3_list.append(n%3)
        n = n//3
        # print("------")
    n3_list.append(n)
    print("3n:",n3_list)
    answer = 0
    a = 0
    while n3_list != []:
        b = n3_list.pop()
        # print(b)
        # print(3**a * b)
        answer += 3 ** a * b
        a += 1
        # print("---")
    # print(answer)
    return answer