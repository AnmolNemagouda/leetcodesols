class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        new=[]
        new.append(0)
        a=0+gain[0]
        new.append(a)
        for i in range(1,len(gain)):
            b=new[i]+gain[i]
            new.append(b)

        return max(new)