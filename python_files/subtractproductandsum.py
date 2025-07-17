class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums=0
        prod=0
        newn=list(str(n))
        sums=int(newn[0])
        prod=int(newn[0])
        for i in range(1,len(newn)):
            sums+=int(newn[i])
            prod*=int(newn[i])
        return prod-sums
