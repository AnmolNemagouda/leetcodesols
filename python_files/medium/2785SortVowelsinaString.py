class Solution:
    def sortVowels(self, s: str) -> str:
        a=[]
        t=list(s)
        b=[]
        for i in range(0,len(s)):
            if s[i]=='A' or s[i]=='a' or s[i]=='E' or s[i]=='e' or s[i]=='I' or s[i]=='i' or s[i]=='O' or s[i]=='o' or s[i]=='U' or s[i]=='u':
                a.append(ord(s[i]))
                b.append(i)
                t.remove(s[i])
        a=sorted(a)
        for i in range(0,len(b)):
            k=chr(a[i])
            t.insert(b[i],k)
        return ''.join(t)

                