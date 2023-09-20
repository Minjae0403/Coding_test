N = int(input())
answer = []
def function(N,i):
    answer.append((N-i-1) * ' '+ i * '*' + '*' + i * '*')
for i in range(2*N-1):
    if i < N:
        function(N,i)        
    else:
        i = 2*(N-1)-i
        function(N,i)

for i in answer:
    print(i)
