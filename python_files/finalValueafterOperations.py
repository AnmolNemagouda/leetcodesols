class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        for i in operations:
            if i=="--X" or i=="X--":
                X-=1
            else:
                X+=1
        return X
            