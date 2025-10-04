class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for i in operations:
            if isinstance(i, str) and i.lstrip('-').isdigit():
                score.append(int(i))
            elif i=='C':
                score.pop(-1)
            elif i=='D':
                score.append(score[-1]*2)
            elif i=='+':
                sums=score[-1]+score[-2]
                score.append(sums)
        if len(score)>0:
            sums=0
            for j in score:
                sums+=int(j)
            return sums
        return 0