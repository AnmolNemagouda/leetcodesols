class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        x=nums[-1]
        missing=[]
        for i in range(nums[0],x+1):
            if i not in nums:
                missing.append(i)
        return missing
