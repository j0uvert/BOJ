def preorder(node):
    global cnt
    if node.children == []:
        cnt += 1
    for child in node.children:
        preorder(tree[child])

class Node:
    def __init__(self):
        self.children = []
    def setChild(self, node):
        self.children.append(node)
    def removeChild(self, node):
        self.children.remove(node)

n = int(input())
inp = list(map(int, input().split()))
tree = [Node() for _ in range(n)]
cnt = 0

for i in range(n):
    if inp[i] != -1:
        tree[inp[i]].setChild(i)

nodeToDelete = int(input())
if inp[nodeToDelete] == -1:
    cnt = 0
else:
    tree[inp[nodeToDelete]].removeChild(nodeToDelete)
    preorder(tree[inp.index(-1)])

print(cnt)