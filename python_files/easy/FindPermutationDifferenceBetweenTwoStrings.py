class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sums=0
        for i in range(0,len(s)):
            for j in range(0,len(t)):
                if s[i]==t[j]:
                    sums+=abs(i-j)
        
        return sums
