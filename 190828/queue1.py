
N = 10
Q = [0] * 10
front = rear = -1


# 원형큐
def enqueue(item):
    global rear
    # full 상태 체크
    if front == (rear + 1) % N: return
    rear = (rear+1) % N
    Q[rear] = item

def dequeue():
    global front
    if front == rear: return
    front = (front+1) % N
    return Q[front]

Q = []
Q.append(1)
while len(Q) > 0:
    Q.pop(0)
