class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        moves=[]
        for i,val in enumerate(boxes):
            add=0
            for j in range(len(boxes)):
                if j!=i and boxes[j]=='1':
                    add+=abs(j-i)
            moves.append(add)
        return moves