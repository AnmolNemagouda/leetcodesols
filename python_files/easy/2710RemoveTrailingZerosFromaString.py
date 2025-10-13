class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        newnum=""
        num=num[::-1]
        for i in range(0,len(num)):
            while num[i]=='0':
                i+=1
            newnum+=num[i:]
            break
        newnum=newnum[::-1]
        return newnum
