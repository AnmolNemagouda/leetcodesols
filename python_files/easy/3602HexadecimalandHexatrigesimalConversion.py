class Solution:
    def concatHex36(self, n: int) -> str:
        hd=n*n
        ht=n**3
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        htn=""
        hx=""
        while hd!=0:
            rem=hd%16
            hx+=digits[rem]
            hd//=16
        hx=hx[::-1]

        while ht!=0:
            rm=ht%36
            htn+=digits[rm]
            ht//=36
        htn=htn[::-1]
        return hx+htn