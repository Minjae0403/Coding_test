from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    def compare(a,b):
        if int(a+b) > int(b+a):
            return -1 #먼저 들어온 요소가 앞으로 정렬됨 a b
        elif int(a+b) < int(b+a):
            return 1 #먼저 들어온 요소가 뒤로 정렬 b a
        else:
            return 0
    numbers.sort(key=cmp_to_key(compare))
    # print(''.join(numbers))
    answer = str(int(''.join(numbers)))
    return answer