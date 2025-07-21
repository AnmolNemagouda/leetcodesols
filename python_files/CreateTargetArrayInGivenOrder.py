class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        nl=[]
        for i in range(0,len(nums)):
            nl.insert(index[i],nums[i])
            
        return nl