# Generic Object Class used by both lists
class Object:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


# List based stack
# Time complexity of O(1)
class ListBasedStack:
    def __init__(self):
        self.stack = []

    def push(self, object):
        self.stack.append(object)
        print(f"Pushed object: {object.getName()} to stack")

    def pop(self):
        if len(self.stack) >= 1:
            print(f"Popped object: {self.stack.pop().getName()} from the stack")


# Create a Linked List Node class designed for use in a Queue
class LinkedListNode:
    def __init__(self, object):
        self.object = object
        self.next = None

    def setObj(self, object):
        self.object = object

    def getObj(self):
        return self.object

# Queue implemented using the linked list data structure
# Time complexity of O(1)
class LinkedListQueue:
    def __init__(self):
        self.tail = None
        self.head = None

    # Utility function to check the length of the queue
    def queueLength(self):
        size = 0
        if(self.head):
            thisNode = self.head
            while(thisNode):
                size += 1
                thisNode = thisNode.next
        return size


    # Enqueue, or insert at beginning of linked list
    def enqueue(self, object):
        newNode = LinkedListNode(object)

        if self.tail is None:
            self.tail = newNode
            self.head = newNode
            print(f"Enqueuing object: {newNode.getObj().getName()}")
            return

        self.tail.next = newNode
        self.tail = newNode
        print(f"Enqueuing object: {newNode.getObj().getName()}")

    # Dequeue, or remove last node from linked list
    def dequeue(self):
        if self.queueLength() == 0:
            return None

        thisNode = self.head
        self.head = thisNode.next
        if(self.head == None):
            self.tail = None

        thisNode.next = None
        print(f"Dequeuing object: {thisNode.getObj().getName()}")
        return thisNode



obj1 = Object("obj1")
obj2 = Object("obj2")
obj3 = Object("obj3")
obj4 = Object("obj4")

list = LinkedListQueue()

list.enqueue(obj1)
list.enqueue(obj2)
list.enqueue(obj3)
list.enqueue(obj4)
print(list.queueLength())
list.dequeue()
list.dequeue()
list.dequeue()
list.dequeue()
list.dequeue()
list.dequeue()
list.dequeue()
list.dequeue()

stack = ListBasedStack()
stack.push(obj1)
stack.pop()
stack.pop()
stack.push(obj1)
stack.push(obj2)
stack.push(obj3)
stack.push(obj4)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()


