class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts={}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        a=[]
        for i,j in counts.items():
            a.append(j)
        b=0
        while a!=[]:
            c=max(a)
            b+=c
            a.remove(c)
            if a==[]:
                break
            d=max(a)
            if d!=c:
                break
        return b


