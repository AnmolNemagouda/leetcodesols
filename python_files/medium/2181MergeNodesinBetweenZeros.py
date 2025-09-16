# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head.next
        total=0
        a=[]
        while itr:
            if itr.val!=0:
                total+=itr.val
            else:
                a.append(total)
                total=0
            itr=itr.next
        new_head = None
        for i in a:
            if new_head is None:
                new_head = ListNode(i, None)
                tail=new_head
            else:  

                tail.next = ListNode(i, None)
                tail=tail.next
        return new_head
