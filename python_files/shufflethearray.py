class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s=[]
        for i in range(0,n):
            for j in range(n+i,len(nums)):
                s.append(nums[i])
                s.append(nums[j])
                break
               
        return s