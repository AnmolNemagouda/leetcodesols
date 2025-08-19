class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count=0
        current=0
        for i in nums:
            if i==0:
                current+=1
                count+=current
            else:
                current=0

        return count