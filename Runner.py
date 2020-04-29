from LinkedList import LinkedList

myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(10))
#print(myList.addNode(5))
print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())
myList.removeNode(10)
print("Size")
print(myList.getSize())
print("Printing")
myList.printNode()

