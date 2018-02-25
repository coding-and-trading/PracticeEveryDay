from LNode import LNode

class LinkedListUnderflow(ValueError):
    pass

class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head._next
        return e