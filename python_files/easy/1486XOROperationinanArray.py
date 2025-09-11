class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(0,n):
            a=start+2*i
            nums.append(a)
        total=0
        for i in nums:
            total=i^total
        return total
            
