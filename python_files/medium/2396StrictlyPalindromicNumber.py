class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        num=n
        bases=[]
        if num==4:
            return False
        elif num>4:
            digits=[]
            check=[]
            for i in range(2,num-1):
                while num>0:
                    digits.append("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[num % i])
                    num//=i
                    check=''.join(reversed(digits))
                if check[:]==check[::-1]:
                    bases.append(i)
        if len(bases) != num - 3:
            return False
        
        return True
