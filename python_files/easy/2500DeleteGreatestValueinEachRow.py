class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        sums=0
        while len(grid)>0:
            b=[]
            for i in grid:
                if i==[]:
                    grid.remove(i)
                    break
                c=max(i)
                b.append(c)
                i.remove(c)
            if b!=[]:
                a=max(b)
                sums+=a    
        return sums