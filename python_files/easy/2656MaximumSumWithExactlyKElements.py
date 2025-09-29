class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sums=0
        if k==1:
            return max(nums)
        while k!=0:
            a=max(nums)
            nums.remove(a)
            sums+=a
            nums.append(a+1)
            k-=1
        return sums