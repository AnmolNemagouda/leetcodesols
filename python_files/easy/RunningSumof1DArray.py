class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=0
        nl=[]
        for i in range(0,len(nums)):
            sums+=nums[i]
            nl.append(sums)
        return nl