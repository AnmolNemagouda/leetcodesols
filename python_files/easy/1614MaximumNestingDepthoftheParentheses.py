class Solution:
    def maxDepth(self, s: str) -> int:
        counter=0
        maxi=0
        for i in range(0,len(s)):
            if s[i]=='(':
                counter+=1

            elif s[i]==')':
                if counter>maxi:
                    maxi=counter
                counter-=1
        return maxi