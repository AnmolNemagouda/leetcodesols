class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts={}
        a=nums.copy()
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        for i,j in counts.items():
            if j>1:
                while j>0:
                    a.remove(i)
                    j-=1
        sums=0
        for i in a:
            sums+=i
        return sums