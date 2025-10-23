class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        altsums=0
        for i in range(0,len(nums)):
            if i%2==0:
                altsums+=nums[i]
            else:
                altsums-=nums[i]
        return altsums