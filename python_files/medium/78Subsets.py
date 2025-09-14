class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[[]]
        for i in nums:
            a+=[s+[i] for s in a]
        return a