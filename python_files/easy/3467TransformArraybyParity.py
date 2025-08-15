class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        new=[]
        for i in nums:
            if i%2==0:
                new.append(0)
            else:
                new.append(1)
        return sorted(new)