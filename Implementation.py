from Stack import Stack
class Implementation:

    def __init__(self):
        self.element = []


    def push(self, element):
        new = Stack(element, top)
        self.top = new
        self.top += 1
        return True

    def pop(self):
        return self.element.pop()

    def top(self):
        return self.element[len(self.element)-1]

    def isemplty(self):
        if self.element == []:
            return True
        else:
            return False
    def size(self):
        return len(self.element)

