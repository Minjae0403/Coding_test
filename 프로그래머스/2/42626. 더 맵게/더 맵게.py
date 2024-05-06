import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    # print(scoville)
    a = heapq.heappop(scoville)
    answer = 0
    while a < K:
        if len(scoville) == 0:
            answer = -1
            break
        b = heapq.heappop(scoville)
        c = a + b * 2 
        
        heapq.heappush(scoville, c)
        
        a = heapq.heappop(scoville)
        answer += 1
    return answer