# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList1 = []
        newList2 = []

        while list1 is not None:
            newList1.append(list1.val)
            list1 = list1.next
        
        while list2 is not None:
            newList2.append(list2.val)
            list2 = list2.next
        
        finList = sorted(newList1 + newList2)

        if not finList:
            return None

        head = ListNode(finList[0])
        current = head

        for i in range(1, len(finList)):
            current.next = ListNode(finList[i])
            current = current.next

        return head
