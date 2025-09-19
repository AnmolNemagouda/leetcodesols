# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        itr=head
        k=[]
        while itr:
            k.append(str(itr.val))
            itr=itr.next
        a=''.join(k)
        return (int(a,2))
        