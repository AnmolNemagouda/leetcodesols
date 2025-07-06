class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumlist=[]
        for i in accounts:
            sum=0
            for num in range(0,len(i)):
                sum+=i[num]
            sumlist.append(sum)
        
        return max(sumlist)