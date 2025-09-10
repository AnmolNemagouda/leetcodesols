class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sublists=[[]]
        for i in nums:
            sublists+=[s + [i] for s in sublists]
        sums=0
        for i in sublists:
            if i==[]:
                sums+=0
            else:
                x=0
                for j in range(0,len(i)):
                    x=x^i[j]
                sums+=x
        return sums
