class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
      
        for i in words:
            j=0
            while j<len(i):
                if i[j] not in allowed:
                    break
                j+=1
            else:
                count+=1

        

        return count
