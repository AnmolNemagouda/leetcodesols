class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            a=i
            b=n-i
            c=str(a)
            d=str(n-i)
            if '0' in c:
                continue
            elif '0' in d:
                continue
            else:
                return [a,b]

            