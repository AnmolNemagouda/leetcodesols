class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        for i in range(0,len(nums)//2):
            a=min(nums)
            b=max(nums)
            c=(a+b)/2
            avg.append(c)
            nums.remove(a)
            nums.remove(b)
        return min(avg)