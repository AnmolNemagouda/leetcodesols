class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sums=0
        sums1=0
        for i in nums:
            if i<10:
                sums+=i
            else:
                sums1+=i
        if sums<sums1 or sums>sums1:
            return True
        
        return False