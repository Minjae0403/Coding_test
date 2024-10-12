def solution(n, m):
    if n>m:
        n, m = m, n
    # print('m:',m)
    # print('n:',n)
    # print(m%n) #m에서 n으로 나눈 나머지
    # print(m//n) #M에서 N으로 나눈 몫
    a = n
    b = m%n
    c = 0
    # print('a:',a) #얘가 최대공약수
    # print('b:',b)
    # print('c:',c)
    while b!=0 : #b가 0인 경우 끝난다.
        # print('0이 아닌경우')
        a, b = b , a%b
        # print('a:',a) #얘가 최대공약수
        # print('b:',b) #얘는 0이 항상 나와야지 정상이다.
    d = int(m*n/a) #최대 공배수는 m*n/최소공배수라는 식을 활용
    # print('d:',d)
    # answer = []
    return [a,d]