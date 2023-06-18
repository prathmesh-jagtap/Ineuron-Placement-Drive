"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4] Output: [7,0,8] Explanation: 342 + 465 = 807.
"""

# Node for linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

      
class Solution:
    def reverse(self, head):
      """ This method use to reverse linked list"""
      if head is None:
          return head

      current = head
      previous = None

      while current is not None:
          temp = current.next
          current.next = previous
          previous = current
          current = temp

      return previous

    def lListSum(self, head1, head2):
        # reversing linked list
        l1 = self.reverse(head1)
        l2 = self.reverse(head2)

        sum = carry = 0
        res = prev = None

        while l1 and l2:

            sum = (carry) + (l1.data if l1 else 0) + (l2.data if l2 else 0)

            carry = (1 if sum >= 10 else 0)

            sum %= 10

            # storing result node
            temp = Node(sum)

            if res is None:
                res = temp
            else:
                prev.next = temp

            prev = temp

            l1 = l1.next
            l2 = l2.next

        if carry > 0:
            temp.next = Node(carry)

        ans = self.reverse(res)
        return ans
