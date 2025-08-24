class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num=nums.copy()
        max1=max(nums)
        num.remove(max1)
        max2=max(num)
        max1-=1
        max2-=1
       
        return max1*max2