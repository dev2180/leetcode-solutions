class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        count = 1
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                count+=i
                if i!=n//i:
                    count+=n//i
        return count==n
            