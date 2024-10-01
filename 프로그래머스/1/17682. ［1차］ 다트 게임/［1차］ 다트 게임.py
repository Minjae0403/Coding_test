import re

def solution(dartResult):
    num_list = re.findall("\d+",dartResult)
    bouns_list = re.findall("\D+",dartResult)
    answer = []
    # print(num_list)
    # print(bouns_list)
    for i in range(len(num_list)):
        bouns = 0
        option = 1
        if bouns_list[i][0] == 'S':
            bouns = 1
        elif bouns_list[i][0] == 'D':
            bouns = 2
        elif bouns_list[i][0] == 'T':
            bouns = 3
        try:
            if bouns_list[i][1] == '#':
                option = -1
            elif bouns_list[i][1] == '*':
                option = 2
                if i != 0:
                    answer[i-1] = answer[i-1] * 2
            # print('num:',num_list[i],'bouns:',bouns,'option:',option)
            # print((int(num_list[i])**bouns)*option)
            answer.append((int(num_list[i])**bouns)*option)
        except:
            # print('num:',num_list[i],'bouns:',bouns,'option:',option)
            # print((int(num_list[i])**bouns)*option)
            answer.append((int(num_list[i])**bouns)*option)
    # print(answer)
    # print(sum(answer))
    # answer = 0
    return sum(answer)