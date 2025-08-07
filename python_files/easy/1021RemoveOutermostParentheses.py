class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        b=list(s)
        s1=[]
        for i in range(0,len(b)):
            if b[i]=='(':
                count+=1
                if count >=2:
                    s1.append('(')
            elif b[i]==')':
                if count>=2:
                    s1.append(')')
                count-=1
                
        return "".join(s1)