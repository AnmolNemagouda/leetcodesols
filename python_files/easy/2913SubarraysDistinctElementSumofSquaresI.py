class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        a=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                a.append(nums[i:j+1])
        sums=0
        for i in a:
            b=set(i)
            sums+=len(b)*len(b)
        return sums