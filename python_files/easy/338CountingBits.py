class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[0]
        for i in range(1,n+1):
            b=bin(i)
            b=str(b)
            b=b[2:]
            count=0
            for j in b:
                if j=='1':
                    count+=1
            a.append(count)
        return a