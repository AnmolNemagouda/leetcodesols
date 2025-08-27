class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a=[]
        k=[]
        for i in range(left,right+1):
            l=list(str(i))
            if '0' not in l:
                count=0
                for j in l:
                    if i%int(j)==0:
                        count+=1
                        if count==len(l):
                            a.append(i)
        return a
