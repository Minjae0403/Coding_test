def solution(s):
    num_dict = {
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }
    answer = ''
    while 0 != len(s):
        if s[0].isdigit():
            answer += s[0]
            s = s[1:]
        else:
            a = 0
            while s[:a] not in num_dict:
                a += 1
            answer += str(num_dict[s[:a]])
            s = s[a:]
    return int(answer)