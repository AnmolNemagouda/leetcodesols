class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i] == '{' or s[i]=='[':
                a.append(s[i])          
            elif s[i]==')':
                if a!=[] and a[-1]=='(':
                    a.pop(-1)            
                else:
                    a.append(')')         
            elif s[i]=='}':
                if a!=[] and a[-1]=='{':
                    a.pop(-1)               
                else:
                    a.append('}')             
            elif s[i]==']':
                if a!=[] and a[-1]=='[':
                    a.pop(-1)              
                else:
                    a.append(']')         
        if a==[]:
            return True
        return False