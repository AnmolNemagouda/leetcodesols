class Solution:
    def minElement(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            new=""
            new+=str(i)
            sum=0
            for j in range(0,len(new)):
                sum+=int(new[j])
            a.append(sum)
        
        return min(a)
                

            
