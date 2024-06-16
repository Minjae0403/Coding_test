class Solution:
    def getLucky(self, s: str, k: int) -> int:
        answer1 = ''
        for i in s:
            answer1 += str(ord(i)-96)
        for i in range(k):
            a = 0
            for i in answer1:
                a += int(i)
            answer1 = str(a)
        return int(answer1)

            
        
        