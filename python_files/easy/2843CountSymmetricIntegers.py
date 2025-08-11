class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count=0
        for i in range(low,high+1):
            a,b=0,0
            s=list(str(i))
            v=len(s)
            z=v//2
            if v%2==0:
                for j in range(0,z):
                    a+=int(s[j])
                for k in range(z,v):
                    b+=int(s[k])
                if a==b:
                    count+=1
        return count
