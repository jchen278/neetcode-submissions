# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        print(stack)
        curr = head
        res = []
        for _ in range((len(stack)-1) // 2):
            tail = stack.pop()

            temp = curr.next
            curr.next = tail
            tail.next = temp

            curr = temp

        if stack:
            new_tail = stack.pop()
            curr.next = new_tail
            curr = new_tail
        curr.next = None

