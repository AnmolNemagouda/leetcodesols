class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        sums=0
        for i in range(0,len(nums)-1,2):
            a=min(nums[i],nums[i+1])
            sums+=a
        return sums
            