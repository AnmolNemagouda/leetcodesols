class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            a=int(i[11])
            b=int(i[12])
            if (a==6 and b>0) or (a>6):
                count+=1
        return count