class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind=0
        for i in range(0,len(word)):
            if word[i]==ch:
                ind=i
                break
        nw=""
        for i in range(0,ind+1):
            nw+=word[i]
        nw=nw[::-1]
        print(nw)
        for i in range(ind+1,len(word)):
            nw=nw+word[i]
        return nw