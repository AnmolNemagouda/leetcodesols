# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        while itr and itr.next:
            a=itr.val
            b=itr.next.val
            
            node=ListNode(gcd(a,b),itr.next)
            itr.next=node
          
            itr=node.next
        return head

