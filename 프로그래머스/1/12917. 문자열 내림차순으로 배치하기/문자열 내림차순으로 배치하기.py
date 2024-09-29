import heapq

def solution(s):
    s = [int(ord(i))for i in list(s)]
    # print(s)
    heapq.heapify(s)
    # print(s)
    s = [chr(i)for i in list(s)]
    # print(s)
    answer = heapq.nlargest(len(s),s)
    # print(answer)
    return ''.join(answer)
