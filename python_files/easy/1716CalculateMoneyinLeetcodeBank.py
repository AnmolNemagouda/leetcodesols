class Solution:
    def totalMoney(self, n: int) -> int:
        amt=0
        mon=1
        cnt=1
        for i in range(1,n+1):
            if i<=7:
                amt+=i
            elif i%7!=1 and i>1:
                amt+=cnt
                cnt+=1
            elif i%7==1:
                mon+=1
                cnt=mon
                amt+=cnt
                cnt+=1
        return amt

