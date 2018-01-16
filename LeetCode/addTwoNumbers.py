import unittest as ut

class TestSolution(ut.TestCase):
    def TestToNumber(self):
        root = ListNode(2)
        node1 = ListNode(4)
        node2 = ListNode(3)

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

    def toNumber(self, x):
        number = 0
        numberes = []
        while x.next is not None:
            numberes.append(x.val)
            x = x.next
        numberes.append(x.val)  # add last one

#        numberes = numberes.reverse()
        for x in  numberes.reverse():

if __name__ == '__main__':