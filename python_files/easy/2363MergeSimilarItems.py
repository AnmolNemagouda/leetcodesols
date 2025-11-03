class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        newweight={}
        for i in items1:
            if i[0] in newweight:
                newweight[i[0]]+=i[1]
            else:
                newweight[i[0]]=i[1]
        for i in items2:
            if i[0] in newweight:
                newweight[i[0]]+=i[1]
            else:
                newweight[i[0]]=i[1]
        
        return sorted(newweight.items())
