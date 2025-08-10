class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        b=[]
        i=0
        a=names.copy()
        z=heights.copy()
        for i in range(0,len(a)):
            s=max(z)
            k=heights.index(s)
            b.append(names[k])
            z.remove(s)
            a.remove(names[k])
            i+=1
        if len(z)==1:
            b.append(a[0])
        return b