class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts={}
        for i in arr:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        
        count=[]
        for i,j in counts.items():
            if j==1:
                count.append(i)
        
        if len(count)>=k:
            return count[k-1]
        else:
            return ""
