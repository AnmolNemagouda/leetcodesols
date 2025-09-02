class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(0,len(nums)):
            if nums[i]<10:
                a.append(nums[i])
            else:
                b=str(nums[i])
                for j in b:
                    a.append(int(j))
        return a