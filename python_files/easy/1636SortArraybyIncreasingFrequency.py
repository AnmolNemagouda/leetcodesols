class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts={}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        a=[]
        
        sorted_dict = dict(sorted(counts.items(), key=lambda item: (item[1], -item[0]))) 
        for i,j in sorted_dict.items():
            while j!=0:
                a.append(i)
                j-=1
        return a

            
            
        