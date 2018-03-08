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

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def print_all(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    def reverse(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q._next = p
            p = q
        self._head = p  #重置表头连接

    def insertAt(self, index, elem):
        count = 0
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        isInsert = False
        while p.next is not None:
            if count is index:
                p.next = LNode(elem)
                isInsert = True
            p = p.next
            count += 1
        if isInsert is not True:
            p.next = LNode(elem)

    def deleteAt(self, index):
       count = 0
       p = self._head
       while p.next is not None:
           if count is index:
               p = p.next.next
            p = p.next
           count += 1


	def for_each(self, proc):
		p = self._head
		while p is not None:
			proc(p.elem)
			p = p.next
if __name__ == '__main__':
