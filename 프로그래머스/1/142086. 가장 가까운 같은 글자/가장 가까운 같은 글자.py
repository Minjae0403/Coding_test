def solution(s):
    num_list=[]
    for num,i in enumerate(s):
        # print("num:",num,"i:",i)
        if num == 0:
            num_list.append(-1)
            # print("0")
        else:
            appendNum = -1
            for j in range(num):
                # print(num-j-1)
                # print(s[num-j-1])
                if s[num-j-1] == i:
                    appendNum = j+1
                    break
            # print(appendNum)
            num_list.append(appendNum)
        # print(num_list)
    # answer = []
    return num_list