class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=-inf
        for i in sentences:
            wo=i.split(' ')
            l=len(wo)
            if l>maxi:
                maxi=l
        
        return maxi
            