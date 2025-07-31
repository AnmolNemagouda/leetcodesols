class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countr=0
        balance=0
        for i in s:
            if i=='R':
                balance+=1
            else:
                balance-=1
            if balance==0:
                countr+=1
        
        return countr