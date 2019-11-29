# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # Ctor
    def __init__(self):
        self.head = None
        self.size = 0

    # isEmpty: return True is the stack is empty
    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False

    # push: push 'data' in the stack
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    # top: return the data of the top node
    def top(self):
        if not self.isEmpty():
            return self.head.data
        else:
            return -1

    # pop: delete the top node and return the data of the node
    def pop(self):
        if not self.isEmpty():
            returnData = self.head.data
            self.head = self.head.next
            self.size -= 1
            return returnData
        else:
            return -1

    # getSize: return 'size'
    def getSize(self):
        return self.size

# input
def inp(stack, returnList):
    n = input().split()
    if n[0] == 'push':
        stack.push(int(n[1]))
    elif n[0] == 'pop':
        returnList.append(stack.pop())
    elif n[0] == 'size':
        returnList.append(stack.getSize())
    elif n[0] == 'empty':
        if stack.isEmpty():
            returnList.append(1)
        else:
            returnList.append(0)
    elif n[0] == 'top':
        returnList.append(stack.top())

if __name__ == "__main__":
    s = Stack()
    n = int(input())
    rl = []
    for i in range(n):
        inp(s, rl)
    for i in rl:
        print(i)
