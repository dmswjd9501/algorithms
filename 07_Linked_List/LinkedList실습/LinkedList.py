class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        print(self.data, '삭제')

class List:
    def __init__(self):
        self.head = None # 빈 리스트인 경우에 None으로 설정
        self.tail = None
        self.size = 0

    def printlist(self):
        if self.head is None: # 항상 공백리스트인지 확인!!!!★
            return

        cur = self.head # 첫번째 노드의 정보를 저장
        print('[', end='')
        while cur is not None: # cur.next is not None:
                                    # while문 끝났을 때 cur은 마지막 노드를 가르키고 있기 때문에
                                    # 마지막이 나오지 않는다
            print(cur.data, end=' ')
            cur = cur.next
        print(']')

    def insertlast(self, node):
        if self.head is None: # 빈 리스트
            self.head = self.tail = node # 사실은 주소를 copy하는 것
            return
        else: # 빈 리스트가 아닐 때 : tail이 node 가르킬 수 있도록
            self.tail.next = node
            self.tail = node
        self.size += 1


    def insertfirst(self, node):
        if self.head is None: # 빈 리스트
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def deletelast(self):
        if self.head is None: # 빈 리스트
            return
            # self.tail = node - 1 => 이거 안됨. 마지막 노드는 알지만, 그 전 노드는 알 수가 없다.
            # 앞에서부터 쭉 따라가는 수 밖에!!

        prev, cur = None, self.head
        while cur.next is not None:
            prev = cur
            cur = cur.next

        if prev is None:
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev

        del cur
        self.size -= 1

    def deletefirst(self):
        if self.head is None:
            return

        # cur가 지울애를 가르키게 하고, 그 다음에를 head로 지정. -> cur을 지운다.
        cur = self.head
        if self.head == self.tail: # 한 개밖에 없는 경우 -> 다 지워버려
            self.head = self.tail = None
        else: # 한 개 이상일 경우 -> cur 다음이 head가 되게한다
            self.head = cur.next

        del cur
        self.size -= 1


    def insertAt(self, idx, node):
        # idx : 삽입 위치, node : 삽입 노드
        # 끼울위치의 앞/뒤에 있는 node 정보를 찾아가면 된다
        if self.head == None: # 빈리스트일때
            self.head = self.tail = node
        else:
            # 원하는 위치만큼 가야함
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None: # 제일 앞쪽에 추가
                node.next = cur
                self.head = node

            elif cur is None: # 범위 벗어남 -> 마지막에 추가
                prev.next = self.tail = node # prev 가 마지막

            else: # 위치 찾아서 추가
                node.next = cur
                prev.next = node

            self.size += 1



    def deleteAt(self, idx):
        pass
