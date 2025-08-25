class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s1=""
        count1=0
        count0=0
        for i in range(0,len(s)):
            if s[i]=='1':
                count1+=1
            else:
                count0+=1
        while count1!=1:
            s1+="1"
            count1-=1
        while count0!=0:
            s1+="0"
            count0-=1
        s1+="1"
            
            
        return s1
