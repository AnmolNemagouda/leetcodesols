class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def mula(num):
            a=str(num)
            f=1
            for i in range(0,len(a)):
                f=f*int(a[i])
            return f
        s=mula(n)
        while True:
            if s%t==0:
                return n
            else:
                n=n+1
                s=mula(n)

            
    



            