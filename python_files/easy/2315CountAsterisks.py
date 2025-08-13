class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        ast=0
        for i in range(0,len(s)):
            if s[i]=='|' and count==0:
                count+=1
            elif s[i] == '|' and count>0:
                count-=1
            if s[i]=='*' and count==0:
                ast+=1
        
        return ast
            
