import itertools

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LinkedList:
    def __init__(self):
        self.head = Node([0, 1, 1, 1, 1, 0])
    
    def addFunction(self, n):
        currentNode = self.head
        for k in range(n+1):
            lst = list(itertools.product([0, 1], repeat=int(k)))
            if len(lst) == 1:
                print(currentNode.data)
            else:
                for i in range(len(lst)):
                    for j in range(k):
                        if lst[i][j] == 0 and currentNode.left:
                            currentNode = currentNode.left
                        elif lst[i][j] == 1 and currentNode.right:
                            currentNode = currentNode.right
                        elif lst[i][j] == 0 and not currentNode.left:
                            currentData = currentNode.data
                            a = currentData[0]
                            b = currentData[1]
                            e = currentData[2]
                            f = currentData[3]
                            c = a + e
                            d = b + f
                            newNode = Node([a, b, c, d, e, f])
                            currentNode.left = newNode
                            print(currentNode.left.data)
                            currentNode = self.head
                        elif lst[i][j] == 1 and not currentNode.right:
                            currentData = currentNode.data
                            a = currentData[2]
                            b = currentData[3]
                            e = currentData[4]
                            f = currentData[5]
                            c = a + e
                            d = b + f
                            newNode = Node([a, b, c, d, e, f])
                            currentNode.right = newNode
                            print(currentNode.right.data)
                            currentNode = self.head
                            
    # This function does not work properly
    def printAll(self, n):
        currentNode = self.head
        for k in range(n+1):
            lst = list(itertools.product([0, 1], repeat=int(k)))
            if len(lst) == 1:
                print(currentNode.data)
            # So the problem is that it only does the last ones and the root, since it only prints when there is nothing else left after it
            else:
                for i in range(len(lst)):
                    for j in range(k):
                        if lst[i][j] == 0 and currentNode.left:
                            currentNode = currentNode.left
                        elif lst[i][j] == 1 and currentNode.right:
                            currentNode = currentNode.right
                        elif lst[i][j] == 0 and not currentNode.left:
                            print(currentNode.data)
                            currentNode = self.head
                        elif lst[i][j] == 1 and not currentNode.right:
                            print(currentNode.data)
                            currentNode = self.head


llist = LinkedList()
n = input()
lst = list(itertools.product([0, 1], repeat=int(n)))
llist.addFunction(int(n))
# llist.printAll(int(n))