class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        else:
            res=[1,2]
            i=2

            while i<n:
                a=res[i-1]+res[i-2]
                res.append(a)
                i+=1

            return res[-1]

    
