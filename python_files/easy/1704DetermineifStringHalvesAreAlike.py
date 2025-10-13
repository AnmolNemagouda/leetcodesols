class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        fl=n//2
        s=s.lower()
        s=list(s)
        fhalf=s[0:fl]
        shalf=s[fl:]
        fcount=0
        scount=0
        for i in fhalf:
            if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
                fcount+=1
        for i in shalf:
            if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
                scount+=1

        if fcount==scount:
            return True
        return False
            