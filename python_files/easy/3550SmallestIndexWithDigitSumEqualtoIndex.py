class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(0,len(nums)):
            sum=0
            b=str(nums[i])
            a=list(b)
            for j in a:
                sum+=int(j)
            if sum==i:
                return i
                break
        return -1
