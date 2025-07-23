class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        counts=0
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]% (nums2[j]*k)==0:
                    counts+=1
        
        return counts