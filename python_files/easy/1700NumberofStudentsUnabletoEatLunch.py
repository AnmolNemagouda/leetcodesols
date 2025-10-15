class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        j=0
        while sandwiches and students:
            if sandwiches[i]==students[j]:
                sandwiches.pop(i)
                students.pop(j)
                continue
            else:
                a=students[j]
                students.pop(j)
                students.append(a)
            if all(s != sandwiches[0] for s in students):
                break
        return len(students)

