class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        a=len(nums)
        c=list(nums)
        counts={}
        s=""
        for i in range(0,a):
            b=bin(i)
            s=str(b)
            for j in s[2:]:
                if j=='1':  
                    if i in counts:
                        counts[i]+=1
                    else:
                        counts[i]=1
        
        for i in range(0,a):
            if i not in counts.keys():
                counts[i]=0
        sums=0
        for key,val in counts.items():
            if val==k:
                sums+=int(c[key])
        return sums

            