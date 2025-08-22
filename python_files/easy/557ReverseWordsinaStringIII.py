class Solution:
    def reverseWords(self, s: str) -> str:
        a=[]
        count=0
        for i in range(0,len(s)):
            if s[i]!=" ":
                a.insert(count,s[i])
            
            elif s[i]==" ":
                count=i+1
                a.append(" ")
                
                
        return "".join(a)