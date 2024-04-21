def solution(genres, plays):
    var_dict = {}
    for i in range(len(genres)):
        if not genres[i] in var_dict:
            var_dict[genres[i]] = plays[i]
        else:
            var_dict[genres[i]] += plays[i]
    # print(var_dict)
    result1 = sorted(var_dict.items(), key = lambda x : x[1])
    result2 = [i for i,_ in result1]
    # print(result1)
    # print(result2)
    a = 0
    for i in var_dict.values():
        if i < 2:
            a += 1
        else:
            a += 2
    var_dict = {}
    for i in range(len(genres)):
        if not genres[i] in var_dict:
            var_dict[genres[i]] = [i]
        elif len(var_dict[genres[i]]) == 1:
            if plays[var_dict[genres[i]][0]] > plays[i]:
                var_dict[genres[i]].append(i)
            else:
                if plays[var_dict[genres[i]][0]] < plays[i]:
                    var_dict[genres[i]] = [i] + var_dict[genres[i]]
                elif plays[var_dict[genres[i]][0]] >= plays[i]:
                    var_dict[genres[i]] = var_dict[genres[i]] + [i]
        else:
            if plays[var_dict[genres[i]][0]] < plays[i]:
                var_dict[genres[i]] = [i, var_dict[genres[i]][0]]
                print('a')
            elif plays[var_dict[genres[i]][0]] == plays[i]:
                var_dict[genres[i]] = [var_dict[genres[i]][0],i]
                print('b')
            elif plays[var_dict[genres[i]][0]] > plays[i] > plays[var_dict[genres[i]][1]]:
                var_dict[genres[i]] = [var_dict[genres[i]][0] ,i]
                print('c')
            else:
                print('d')
                pass
        print(i)
        print(var_dict)
    answer = []
    for i in result2[::-1]:
        answer += var_dict[i]
        # print(answer)
    # answer = []
    return answer