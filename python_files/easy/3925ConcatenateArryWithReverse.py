class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans=nums
        for i in nums[::-1]:
            ans.append(i)
        return ans