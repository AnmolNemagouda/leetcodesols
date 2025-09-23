class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        a=nums.copy()
        for i in nums:
            b=str(i)
            b=b[::-1]
            b=int(b)
            a.append(b)
        a=set(a)
        return len(a)