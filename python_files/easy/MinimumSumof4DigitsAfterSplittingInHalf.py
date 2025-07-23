class Solution:
    def minimumSum(self, num: int) -> int:
        l=sorted(list(str(num)))
        a=l[0]+l[2]
        b=l[1]+l[3]
        c=int(a)+int(b)

        return c