class Solution:
    def minPartitions(self, n: str) -> int:
        b=0
        for i in n:
            a=int(i)
            if a>b:
                b=a
        return b