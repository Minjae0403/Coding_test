import heapq

def solution(d, budget):
    heapq.heapify(d)
    answer = 0
    if sum(d) <= budget:
        answer = len(d)
    else:
        while d and budget >= d[0]:
            budget -= heapq.heappop(d)
            answer += 1
    #         print(a)
    #         print(budget)
    #         print('==')
    # print("answer",answer)
    # print("budget",budget)
    if budget < 0:
        answer -= 1
    # print(answer)
    return answer