class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a=[]
        for i in grid:
            for j in i:
                a.append(j)
        a=sorted(a)
        b=[]
        for i in range(0,len(a)-1):
            if a[i]==a[i+1]:
                b.append(a[i])
        for i in range(1,len(a)+1):
            if i not in a and i!=0:
                b.append(i)
        return b
