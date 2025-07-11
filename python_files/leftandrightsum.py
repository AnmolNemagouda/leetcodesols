class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
       
        right=[]
        left=[]
        for i in range(0,len(nums)):
            leftsum=0
            rightsum=0
            if i==0:
                left.append(leftsum)
                for i in range(i+1,len(nums)):
                    rightsum+=nums[i]
                right.append(rightsum)
            elif i==len(nums)-1:

                right.append(0)
                for i in range(0,len(nums)-1):
                    leftsum+=nums[i]
                left.append(leftsum)
            else:
                for j in range(0,i):
                    leftsum+=nums[j]
                left.append(leftsum)
                for j in range(i+1,len(nums)):
                    rightsum+=nums[j]
                right.append(rightsum)
        answer=[]
        for i,n in list(zip(left,right)):
            answer.append(abs(i-n))

        return answer


            