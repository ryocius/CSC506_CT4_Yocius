# Generic Object Class used by both lists
import timeit


class Object:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


# List based stack
# Time complexity of O(1)
class ListBasedStack:
    def __init__(self, printBool = False):
        self.stack = []
        self.printBool = printBool

    def push(self, object):
        self.stack.append(object)
        if self.printBool:
            print(f"Pushed object: {object.getName()} to stack")

    def pop(self):
        if len(self.stack) >= 1:
            if self.printBool:
                print(f"Popped object: {self.stack.pop().getName()} from the stack")
            else:
                self.stack.pop()


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
    def __init__(self, printBool = False):
        self.tail = None
        self.head = None
        self.printBool = printBool

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
            if self.printBool:
                print(f"Enqueuing object: {newNode.getObj().getName()}")
            return

        self.tail.next = newNode
        self.tail = newNode
        if self.printBool:
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
        if self.printBool:
            print(f"Dequeuing object: {thisNode.getObj().getName()}")
        return thisNode

def functionTest():
    obj1 = Object("obj1")
    obj2 = Object("obj2")
    obj3 = Object("obj3")
    obj4 = Object("obj4")

    list = LinkedListQueue(True)

    list.enqueue(obj1)
    list.enqueue(obj2)
    list.enqueue(obj3)
    list.enqueue(obj4)
    list.dequeue()
    list.dequeue()
    list.dequeue()
    list.dequeue()
    list.dequeue()
    list.dequeue()
    list.dequeue()
    list.dequeue()

    stack = ListBasedStack(True)
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


def perfExperiment():
    SETUP_CODE = '''
from __main__ import Object, ListBasedStack, LinkedListNode, LinkedListQueue  

numObjects = 1000
objects = []
for i in range(numObjects):
    objects.append(Object(f"obj{i}")) 

'''

    STACK_CODE = '''
stack = ListBasedStack()
for j in objects:
    stack.push(j)

for k in objects:
    stack.pop()
'''

    QUEUE_CODE = '''
queue = LinkedListQueue()
for j in objects:
    queue.enqueue(j)
    
for k in objects:
    queue.dequeue()    
'''

    stackTimes = timeit.repeat(stmt=STACK_CODE, setup=SETUP_CODE, repeat=5, number=100)
    print(f"Best list-based stack time = {min(stackTimes)}")
    queueTimes = timeit.repeat(stmt=QUEUE_CODE, setup=SETUP_CODE, repeat=5, number=100)
    print(f"Best linked list queue time = {min(queueTimes)}")




# functionTest()

perfExperiment()

