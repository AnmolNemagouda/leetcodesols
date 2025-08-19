class Solution:
    def replaceDigits(self, s: str) -> str:
        l=list(s)
        if len(s)==1:
            return s
        for i in range(0,len(s)):
            if i%2!=0:
                a=ord(s[i-1])
                a+=int(s[i])
                c=chr(a)
                l.remove(l[i])
                l.insert(i,c)
        return ''.join(l)
