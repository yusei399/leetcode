class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp:
            while temp.next!=None and temp.val == temp.next.val:
                temp.next=temp.next.next
            temp=temp.next
        return head