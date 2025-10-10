class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a=[]
        s=list(s)
        for i in s:
            a.append(s.count(i))
        a=set(a)
        if len(a)==1:
            return True
        return False