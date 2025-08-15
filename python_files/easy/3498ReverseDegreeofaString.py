import string
class Solution:
    def reverseDegree(self, s: str) -> int:
        counts={}
        j=26
        for i in string.ascii_lowercase:
            while j>0:
                counts[i]=j
                break
            j=j-1
        sums=0
        k=1
        for i in s:
            val=counts.get(i)
            while k<=len(s):
                ind=k
                break
            k+=1
            sums+= val*ind
        
        return sums
