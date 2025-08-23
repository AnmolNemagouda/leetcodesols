class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        x= sqrt(((n**2)+n)/2)
        print(x)
        y=int(x)
        if x==y:
            return y
        
        return -1
                