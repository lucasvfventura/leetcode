# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2

        if not list2:
            return list1

        dummy_first = ListNode(0)
        list1_current = list1
        list2_current = list2
        current = dummy_first

        while list1_current != None and list2_current != None:
            if list1_current.val < list2_current.val:
                current.next = list1_current
                list1_current = list1_current.next
            else:
                current.next = list2_current
                list2_current = list2_current.next

            current = current.next

        if list1_current:
            current.next = list1_current
        else:
            current.next = list2_current

        return dummy_first.next