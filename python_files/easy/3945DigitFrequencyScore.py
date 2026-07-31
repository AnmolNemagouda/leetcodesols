class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        dictnum={}
        a=str(n)
        freq=0
        for i in a:
            if i in dictnum:
                dictnum[i]+=1
            else:
                dictnum[i]=1
                count=1
        for key in dictnum:
            freq+=int(key)*dictnum[key]

        return freq
