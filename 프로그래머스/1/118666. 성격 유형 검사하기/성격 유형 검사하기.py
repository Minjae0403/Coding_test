def solution(survey, choices):
    points_dict ={'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for num, i in enumerate(survey):
        # print(num, i)
        # print(choices[num])
        point = choices[num]-4
        # print(point)
        if point < 0:
            points_dict[i[0]] += (-1)*point
        elif point > 0:
            points_dict[i[1]] += point
        # print(points_dict)
        # print("====")
    answer = ''
    if points_dict['R']>=points_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    if points_dict['C']>=points_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    if points_dict['J']>=points_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    if points_dict['A']>=points_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer