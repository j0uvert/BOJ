
# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue
class Queue:
    # Ctor
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0

    # isEmpty: return True if the queue is empty, and False if not
    def isEmpty(self):
        if not self.front:
            return True
        else:
            return False

    # enqueue: insert 'data' in the queue
    def enqueue(self, data):
        tempNode = Node(data)
        if self.isEmpty():
            self.front = tempNode
            self.rear = tempNode
            self.size += 1
            return
        else:
            self.rear.next = tempNode
            self.rear = tempNode
            self.size += 1

    # dequeue: pop
    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            returnData = self.front.data
            self.front = self.front.next
            self.size -= 1
            return returnData

    # getFront: return the data of the front
    def getFront(self):
        if self.isEmpty():
            return -1
        else:
            return self.front.data

    # getRear: return the data of the rear
    def getRear(self):
        if self.isEmpty():
            return -1
        else:
            return self.rear.data

    # getSize: return the size of the queue
    def getSize(self):
        return self.size

# input
def inp(queue, returnList):
    n = input().split()
    if n[0] == 'push':
        queue.enqueue(int(n[1]))
    elif n[0] == 'pop':
        returnList.append(queue.dequeue())
    elif n[0] == 'size':
        returnList.append(queue.getSize())
    elif n[0] == 'empty':
        if queue.isEmpty():
            returnList.append(1)
        else:
            returnList.append(0)
    elif n[0] == 'front':
        returnList.append(queue.getFront())
    elif n[0] == 'back':
        returnList.append(queue.getRear())

if __name__ == "__main__":
    n = int(input())
    q = Queue()
    rl = []
    for i in range(n):
        inp(q, rl)
    for i in rl:
        print(i)
