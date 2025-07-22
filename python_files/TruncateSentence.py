class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split(" ")
        w=""
        w+=s[0]
        for i in range(1,len(s)):
            if i<k:
                w+=" "+s[i]
        return w