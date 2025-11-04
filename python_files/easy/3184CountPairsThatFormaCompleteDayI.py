class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        complete=0
        for i in range(0,len(hours)-1):
            for j in range(i+1,len(hours)):
                a=hours[i]+hours[j]
                if a%24==0:
                    complete+=1
        return complete
