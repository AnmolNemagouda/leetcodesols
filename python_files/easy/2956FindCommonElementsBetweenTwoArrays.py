class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts=0
        l=[]
        for i in nums1:
            if i in nums2:
                counts+=1
        l.append(counts)
        ncount=0
        for i in nums2:
            if i in nums1:
                ncount+=1
        l.append(ncount)

        return l
