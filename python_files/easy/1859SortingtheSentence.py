class Solution:
    def sortSentence(self, s: str) -> str:
        k=s.split(" ")
        new=[""]*len(k)
        for i in k:
            num=int(i[-1])
            new[num-1]=i[0:-1]
        return " ".join(new)

            