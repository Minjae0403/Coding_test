# 1. map으로 체육복 갯수를 표현
# 2. 조건문으로 앞뒤의 체육복을 가져오는 것으로 구현
# 3. value가 0 인 경우만 빼기

def solution(n, lost, reserve):
    # 1. map으로 체육복 갯수를 표현
    map_a = {}
    for i in range(1,n+1):
        map_a[i] = 1
    for i in lost:
        map_a[i] -= 1
    for i in reserve:
        map_a[i] += 1
    # 2. 조건문으로 앞뒤의 체육복을 가져오는 것으로 구현
    for a in map_a:
        if map_a[a] == 0:
            if a > 1 and a < n:
                if map_a[a-1] == 2:
                    map_a[a-1] = 1
                    map_a[a] = 1
                elif map_a[a+1] == 2:
                    map_a[a+1] = 1
                    map_a[a] = 1
            elif a == 1:
                if map_a[a+1] == 2:
                    map_a[a+1] = 1
                    map_a[a] = 1
            elif a == n:
                if map_a[a-1] == 2:
                    map_a[a-1] = 1
                    map_a[a] = 1
    # 3. value가 0 인 경우만 빼기
    answer = n
    for b, c in map_a.items():
        if c == 0:
            answer -= 1
    return answer