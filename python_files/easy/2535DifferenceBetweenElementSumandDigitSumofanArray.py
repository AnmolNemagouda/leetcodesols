class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        e=0
        d=0
        for i in nums:
            e+=i
            a=str(i)
            for j in range(0,len(a)):
                d+=int(a[j])
        a=e-d
        return a