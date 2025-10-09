class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)//2
        k=[]
        while len(k)!=n:
            a=nums[0]
            nums.pop(0)
            if a in nums:
                b=a
                nums.remove(b)
                k.append([a,b])
            else:
                return False
        if len(k)==n:
            return True

