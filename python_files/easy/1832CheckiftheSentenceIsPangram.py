class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counts={}
        for i in range(0,len(sentence)):
            if sentence[i] in counts:
                counts[sentence[i]]+=1
            else:
                counts[sentence[i]]=1
        if len(counts)==26:
            return True
        return False