class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                nums[i]+=1
                count+=1
            elif nums[i]<nums[i-1]:
                a=nums[i-1]-nums[i]
                a+=1
                nums[i]+=a
                count+=a
        return count
            