class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        new=[]
        for i in range(0,len(prices)):
            newp=prices[i]
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i] and len(new)<=i:
                    newp=prices[i]-prices[j]
                    new.append(newp)
            if len(new)<=i:
                new.append(newp)                

        return new
        
        