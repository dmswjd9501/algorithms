class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        tmp = []
        if self.head is None:
            return
        cur = self.head
        while cur is not None:
            tmp.append(cur.data)
            cur = cur.next
        return tmp

    def insertlast(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertAt(self, idx, node):
        if self.head == None:
            self.head = self.tail = node
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1
            if prev is None:
                node.next = cur
                self.head = node
            elif cur is None:
                prev.next = self.tail = node
            else:
                node.next = cur
                prev.next = node
            self.size += 1