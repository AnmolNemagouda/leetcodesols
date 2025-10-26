class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        kc=""
        while n!=0:
            rm=n%k
            kc+=digits[rm]
            n//=k
        sumk=0
        for i in kc:
            sumk+=int(i)
        return sumk
