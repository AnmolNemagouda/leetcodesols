class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mins=2**10
        for i in tasks:
            sums=0
            for j in i:
                sums+=j
            if sums<=mins:
                mins=sums
        return mins

