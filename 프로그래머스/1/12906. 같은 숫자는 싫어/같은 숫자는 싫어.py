def solution(arr):
    befor_arr = arr[0]
    # print(befor_arr)
    answer = [befor_arr]
    for i in arr[1:]:
        now_arr = i
        if now_arr != befor_arr:
            answer.append(i)
            befor_arr = i
    return answer