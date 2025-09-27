class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums3=nums1+nums2
        nums3=sorted(nums3)
        new=[]
        counts={}
        for i in nums3:
            if i[0] in counts:
                counts[i[0]]+=i[1]
            else:
                counts[i[0]]=i[1]
        for i,j in counts.items():
            a=[i,j]
            new.append(a)
        return new
