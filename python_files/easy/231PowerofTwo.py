class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n>1:
            if n%2!=0:
                return False
            else:
                for i in range(1,31):
                    if 2**i==n:
                        return True
        return False