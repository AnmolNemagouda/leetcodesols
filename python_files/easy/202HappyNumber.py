class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        if n<10 and n>=2:
            res=n*n
        else:
            res=n
        while res!=1:
            a=str(res)
            l=list(a)
            res=0
            for i in l:
                i=int(i)
                b=i*i
                res+=b
            if res<5:
                break
        if res==1:
            return True
        return False