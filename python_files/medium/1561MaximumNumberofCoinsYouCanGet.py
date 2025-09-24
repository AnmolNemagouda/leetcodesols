class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles)
        me=0
        a=len(piles)//3
        for i in range(a,len(piles),2):
            me+=piles[i]
        return me