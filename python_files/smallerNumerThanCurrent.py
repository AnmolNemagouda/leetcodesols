class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=[]
        for i in range(0,len(nums)):
            counts=0
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    counts+=1
            s.append(counts)

        return s
