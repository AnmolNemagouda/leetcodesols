class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sums=0
        seats=sorted(seats)
        students=sorted(students)
        for i in range(0,len(seats)):
            if students[i]==seats[i]:
                sums+=0
            elif students[i]>seats[i]:
                sums+=(students[i]-seats[i])
            else:
                sums+=(seats[i]-students[i])
        return sums