class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a=len(pref)
        count=0
        
        for i in words:
            if len(i)>=len(pref):
                counter=0
                for j in range(0,len(pref)):
                    if i[j]==pref[j]:
                        counter+=1
                if counter==len(pref):
                    count+=1
        return count

