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
        if self.head == None: # 빈공간이면 그냥 추가
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

    def deleteAt(self, idx):
        if self.head == None: # 빈 리스트
            return
        else:
            # 원하는 위치까지 가기
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if self.head == self.tail: # 한개밖에 없는 경우 -> 다 지우기
                self.head = self.tail = None

            elif cur is None: # 범위를 벗어난 경우 -> 마지막을 제거
                prev.next = None
                self.tail = prev

            else: # 그 외 -> 위치 찾아서 제거
                prev.next = cur.next

            del cur
            self.size -= 1


    def changeAt(self, idx, node):
        if self.head == None:
            return
        else:
            # 원하는 위치까지 이동
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1
            if self.head == self.tail: # 한개밖에 없는 경우 -> node추가
                self.head = self.tail = node
            elif cur is None: # 범위를 벗어난 경우
                return
            else: # 그 외는 -> 위치 찾아서 데이터 변경
                cur.data = node


