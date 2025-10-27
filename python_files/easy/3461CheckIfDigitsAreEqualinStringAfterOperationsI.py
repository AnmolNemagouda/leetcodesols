class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s)==2 and s[0]:
            return s
        while len(s)!=2:
            new=""
            for i in range(0,len(s)-1):
                
                if len(s)==2:
                    return s
                a=(int(s[i])+int(s[i+1]))%10
                new+=str(a)
            s=new
            if len(s)==2:
                break
        if len(s)==2 and s[0]==s[1]:
            return True
        return False
            

