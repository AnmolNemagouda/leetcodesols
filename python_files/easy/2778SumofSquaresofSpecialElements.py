class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sums=0
        n=len(nums)
        for i in range(0,n):
            if i==0:
                sums+=nums[i]*nums[i]
            elif i!=0:
                if n%(i+1)==0:
                    sums+= nums[i]*nums[i]
        return sums
