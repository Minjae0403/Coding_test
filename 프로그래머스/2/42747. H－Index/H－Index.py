def solution(citations):
    citations.sort()
    # print(citations)
    h = 0
    for i in range(len(citations)):
        a = len(citations) - i - 1
        # print(i)
        # print(citations[a])
        # print(citations[i:])
        # print(len(citations[i:]))
        # print(len(citations[:i]))
        # print('===')
        if i >= citations[a]:
            h = i
            print(i)
            break
        h = i
        if i == len(citations)-1: #길이 끝까지 가는경우
            h += 1
    # answer = 0
    return h