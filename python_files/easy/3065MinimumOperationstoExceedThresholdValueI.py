class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        a=min(nums)
        while a<k:
            b=min(nums)
            nums.remove(b)
            count+=1
            a=min(nums)
        return count
        #a=nums.copy()
        #for i in nums:
            #if i<k:
                #a.remove(i)
                #count+=1
        #return count