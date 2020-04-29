from Node import Node
class LinkedList:

    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        print('data is:',data)
        print('self head before creating node',self.head)
        newNode = Node(data, self.head)
        print('newNode is', newNode)
        self.head = newNode
        print('print what is self.head',self.head)
        self.size+=1
        return True

    def printNode(self):
        curr = self.head
        print(curr)
        while curr:
            print(curr.data)

            curr = curr.getNextNode()

    def removeNode(self, x):
        curr = self.head
        print("Printing Curr", curr)
        print("Printing data inside curr", curr.nextNode)
        prev = None

        while curr is not None:
            if curr.getData() == x:
                print("getData:", curr.getData())
                if prev is not None:
                    x = curr.nextNode
                    prev.setNext(curr.getNextNode())

                else:
                    self.head = curr.getNextNode()
                    self.size -= 1
                    return True

            else:
                prev = curr
                curr = curr.getNextNode()
                return False
