class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mini=[]
        for i in matrix:
            mini.append(min(i))
        maxi= [max(col) for col in zip(*matrix)]
        for x in mini:
            if x in maxi:
                return [x]
        return []
        
                