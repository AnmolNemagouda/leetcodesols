class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        a=text.split()
        b=len(a)
        for i in text.split():
            for j in range(len(i)):
                if i[j] in brokenLetters:
                    count+=1
                    break
        return b-count