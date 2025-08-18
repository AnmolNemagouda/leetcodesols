class Solution:
    def clearDigits(self, s: str) -> str:
        a=list(s)
        count=0
        for i in range(0,len(s)):
            if s[i]=='0' or s[i]=='1' or s[i]=='2' or s[i]=='3' or s[i]=='4' or s[i]=='5' or s[i]=='6' or s[i]=='7' or s[i]=='8' or s[i]=='9':
                
                a.pop(i-count)

                if i!=0:
                    a.pop((i-1)-count)
                    count+=1
                count+=1
        if a==[]:
            return ""
        return ''.join(a)