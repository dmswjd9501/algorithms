class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None # 빈 리스트인 경우에 None으로 설정
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
        if self.head is None:  # 빈 리스트
            self.head = self.tail = node  # 사실은 주소를 copy하는 것
            return
        else:  # 빈 리스트가 아닐 때 : tail이 node 가르킬 수 있도록
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertAt(self, idx, node):
        # idx : 삽입 위치, node : 삽입 노드
        # 끼울위치의 앞/뒤에 있는 node 정보를 찾아가면 된다
        if self.head == None:  # 빈리스트일때
            self.head = self.tail = node
        else:
            # 원하는 위치만큼 가야함
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None:  # 제일 앞쪽에 추가
                node.next = cur
                self.head = node
            elif cur is None:  # 범위 벗어남 -> 마지막에 추가
                prev.next = self.tail = node  # prev 가 마지막
            else:  # 위치 찾아서 추가
                node.next = cur
                prev.next = node

            self.size += 1
