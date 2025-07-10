class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts={}
        for i in range(0,len(s)):
            if s[i] in counts:
                counts[s[i]]+=1
            else:
                counts[s[i]]=1
        s=0
        c=0
        for i in counts:
            if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u') and counts[i]>s:
                s=counts[i]
            elif (i!='a' and i!='e' and i!='i' and i!='o' and i!='u') and counts[i]>c:
                c=counts[i]

        return s+c
