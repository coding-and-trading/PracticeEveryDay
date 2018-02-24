import unittest as ut

def listNodeBuilder(numbers):
    nodes = [ListNode(x) for x in numbers]

    root = nodes[0]
    copy_root = root
    for x in range(1, len(nodes)):
        root.next = nodes[x]
        root = root.next

    return copy_root

class TestSolutionMethods(ut.TestCase):
    def test_toNumber(self):
        numbers = [ 2, 4, 3 ]
        root = listNodeBuilder(numbers)
        s = Solution()
        self.assertEqual(342, s.toNumber(root))

    def testAddTwoNumbers(self):
        number1, number2 = listNodeBuilder([2, 4, 3]), listNodeBuilder([5, 6, 4])
        result = listNodeBuilder([7, 0, 8])

        s = Solution()

        self.assertEqual(s.toNumber(result),
                        s.toNumber(s.addTwoNumbers(number1, number2)))

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
        total = str(self.toNumber(l1) + self.toNumber(l2))

        node_element = [ListNode(x) for x in reversed(total)]
        root = node_element[0]
        copy_root = root
        for x in range(1, len(node_element)):
            root.next = node_element[x]
            root = root.next

        return copy_root

    def toNumber(self, x):
        number = 0
        numberes = []
        while x.next is not None:
            numberes.append(x.val)
            x = x.next
        numberes.append(x.val)  # add last one
        numberes = reversed(numberes)
        for x in numberes:
            number = int(number) * 10 + int(x)

        return number

if __name__ == '__main__':
    ut.main()