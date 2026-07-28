# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revList = []
        while True:
            if head is not None:
                revList.append(head.val)
                if head.next is None:
                    break
                head = head.next
            else:
                return head

        
        newList = []
        for i in range(len(revList) - 1, -1, -1):
            newList.append(revList[i])
        
        head = ListNode(newList[0])
        current = head

        for i in range(1, len(newList)):
            current.next = ListNode(newList[i])
            current = current.next
        
        return head