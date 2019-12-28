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
            return None

if __name__ == "__main__":
    s = Stack()
    result = []
    output = []
    n = int(input())

    for _ in range(n):
        result.append(int(input()))

    resultNow = 1

    for i in range(n):
        if i == 0:
            while resultNow <= result[i]:
                s.push(resultNow)
                output.append('+')
                resultNow += 1
            s.pop()
            output.append('-')
        else:
            if result[i] < result[i - 1]:
                if s.top() == result[i]:
                    s.pop()
                    output.append('-')
                else:
                    output.append("NO")
                    break
            else:
                while resultNow <= result[i]:
                    s.push(resultNow)
                    output.append('+')
                    resultNow += 1
                s.pop()
                output.append('-')

    print(resultNow)
    print(output)