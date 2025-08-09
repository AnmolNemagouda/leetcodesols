class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        l=list(str(x))
        sum=0
        for i in l:
            sum+=int(i)
        if x%sum==0:
            return sum
        return -1
