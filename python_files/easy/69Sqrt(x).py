class Solution:
    def mySqrt(self, x: int) -> int:
        right=(x//2) +1
        left=0
        interim=0
        if x==0:
            return 0
        else:
            while left<=right:
                mid=(left+right)//2
                a=mid*mid
                if a==x:
                    return mid
                elif a>x :
                    right=mid-1
                elif a<x:
                    interim=mid
                    left=mid+1

                
            return interim
        
        
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         right=(x//2) +1
#         left=0
#         if x==0:
#             return 0
#         else:
#             while left<=right:
#                 mid=(left+right)//2
#                 a=mid*mid
#                 b=mid+1
#                 c=b*b
#                 d=mid-1
#                 e=d*d
#                 if a==x or (a<x and c>x):
#                     return mid
#                 elif a>x and e<=x:
#                     return mid-1
#                 if a>x :
#                     right=mid-1
#                 elif a<x:
#                     left=mid+1

                