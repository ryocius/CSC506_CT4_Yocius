
class Object:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)


# Create a Linked List Node class designed for use in a Queue
class LinkedListNode:
    def __init__(self, object):
        self.object = object
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None

    # Enqueue, or insert at beginning of linked list
    def enqueue(self, object):
        new_node = LinkedListNode(object)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def listLength(self):
        size = 0
        if(self.head):
            thisNode = self.head
            while(thisNode):
                size += 1
                thisNode = thisNode.next
        return size

    # Dequeue, or remove last node from linked list
    def dequeue(self):
        if self.head is None:
            return None

        thisNode = self.head
        if self.listLength() == 1:
            return thisNode
        else:
            while(thisNode.next.next):
                thisNode = thisNode.next

        thisNode.next = None
        return thisNode



obj1 = Object("obj1")
obj2 = Object("obj2")
obj3 = Object("obj3")
obj4 = Object("obj4")

list = LinkedListQueue()
list.enqueue(obj1)
list.dequeue().object.printName()

list.enqueue(obj1)
list.enqueue(obj2)
list.enqueue(obj3)
list.enqueue(obj4)
list.dequeue().object.printName()
list.dequeue().object.printName()
list.dequeue().object.printName()
list.dequeue().object.printName()
list.dequeue().object.printName()