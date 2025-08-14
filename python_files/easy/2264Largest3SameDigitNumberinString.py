class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums=-inf
        x=len(num)-3
        if x==0:
            if num[0]==num[1] and num[0]==num[2]:
                if num[0]!=0:
                    return num
                elif num[0]==0:
                    return "000"
            else:
                return ""                
        for i in range(0,x+1):
            a=""
            if num[i]==num[i+1] and num[i]==num[i+2]:
                a=num[i]+num[i+1]+num[i+2]
                b=int(a)
                if b>nums:
                    nums=b
        if nums==0:
            return "000"
        elif nums==-inf:
            return ""
        else:
            return str(nums)


