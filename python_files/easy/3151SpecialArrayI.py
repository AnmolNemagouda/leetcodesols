class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        count=0
        i=0
        if len(nums)==1:
            return True
        while i<len(nums)-1:
            j=i+1
            if (nums[i]%2==0 and nums[j]%2!=0) or (nums[i]%2!=0 and nums[j]%2==0):
                count+=1
                i+=1
            else:
                break
        if count==len(nums)-1:
            return True
        return False
