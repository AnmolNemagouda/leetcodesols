class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        new=[]
        for i in range(0,n):
            for j in range(i+1,n+1):
                new.append(arr[i:j])
        total=0
        for i in new:
            sum=0
            if len(i)%2 !=0:
                for j in i:
                    sum+=j
                total+=sum
        return total

