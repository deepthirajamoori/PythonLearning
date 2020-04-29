from Node import Node

class Deletelist:

    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size+=1
        return True
    listx = newNode
    print(listx)

    def delete(data):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()
        for i in range(len(curr)):
            print(l)
        curr.remove(data)
        print(curr)





