class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=0
        while x < len(nums):
            for y in range(len(nums)):
                if x!=y:
                    if nums[x]+nums[y] == target:
                        return x,y
            x=x+1

            