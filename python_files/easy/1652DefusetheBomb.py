class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        a=[]
        for i in range(0,len(code)):
            sums=0
            if k>0:
                for j in range(i+1,i+1+k):
                    sums+=code[j%len(code)]
                a.append(sums)
            elif k<0:
                for j in range(i-1,i+k-1,-1):
                    sums+=code[j]
                a.append(sums)
            elif k==0:
                code.pop(i)
                code.insert(i,0)
        if k!=0:
            return a
        return code
