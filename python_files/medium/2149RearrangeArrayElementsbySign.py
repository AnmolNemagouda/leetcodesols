class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        new=[]
        for i in range(len(p)):
            new.append(p[i])
            new.append(n[i])
        return new
