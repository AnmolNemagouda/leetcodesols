class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s=str(num)
        for i in range(0,len(s)):
            a=s[::-1]
        a=int(a)
        b=str(a)
        for i in range(0,len(b)):
            c=b[::-1]
        d=int(c)
        if d==num:
            return True
        return False