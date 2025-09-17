
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        count=0
        while itr:
            count+=1
            itr=itr.next
        itr=head
        if count==1:
            return head
        if count%2==0:
            count=(count//2)
            a=0
            while a<count:
                itr=itr.next
                if a==count-1:
                    return itr
                a+=1
        else:
            count=(count//2)+1
            a=0
            itr=head
            while a<count:
                itr=itr.next
                if a==count-2:
                    return itr
                a+=1
        
