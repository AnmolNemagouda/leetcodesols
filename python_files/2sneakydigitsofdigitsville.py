class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky=[]
        counts={}
        for i in range(0,len(nums)):
            if nums[i] in counts:
                sneaky.append(nums[i])
            else:
                counts[nums[i]]=1
        return sneaky