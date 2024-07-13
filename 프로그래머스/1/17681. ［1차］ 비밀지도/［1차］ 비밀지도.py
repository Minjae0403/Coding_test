def solution(n, arr1, arr2):
    answer_array = [''*n]*n
    print(answer_array)
    print('arr1')
    for i in range(len(arr1)):
        b0_num = bin(arr1[i])[2:]
        while len(b0_num) != n:
            b0_num = '0'+ b0_num
        print('숫자 :',arr1[i], ' / 이진수 :', b0_num)
        answer_array[i] = list(b0_num)
    print('answer_array:',answer_array)
    print('arr2')
    for i in range(len(arr2)):
        b0_num = bin(arr2[i])[2:]
        while len(b0_num) != n:
            b0_num = '0'+ str(b0_num)
        print('숫자 :',arr2[i], ' / 이진수 :', b0_num)
        for j in range(len(b0_num)):
            # print(b0_num[j])
            # print(answer_array[i][j])
            if answer_array[i][j] == '0' and b0_num[j] == '1':
                # print('yes')
                answer_array[i][j] = '#'
            elif answer_array[i][j] == '0':
                answer_array[i][j] = ' '
            elif answer_array[i][j] == '1':
                answer_array[i][j] = '#'
            # print(f'answer_array[{i}][{j}]:',answer_array[i][j])
            # print('==')
        answer_array[i] = ''.join(answer_array[i])
    # print('answer_array:',answer_array)
    # answer = []
    return answer_array