import sys
import re

class Queue :
    def __init__(self) -> None:
        self.queue = []
    
    def getSize(self) :
        return len(self.queue)
    
    def enqueue(self, value) :
        self.queue.append(value)
    
    def dequeue(self) :
        if self.isEmpty() == True :
            return None
        de_value = self.queue[0]
        self.queue = self.queue[1:]
        return de_value
    
    def isEmpty(self) :
        if len(self.queue) == 0 :
            return True
        else :
            return False
    
    def getInOneLine(self) :
        return " ".join(list(self.queue))
        
class Stack :
    # def __init__(self, size=10):
    #     self.stack = []
    #     self.maxSize = size
    
    # def isEmpty(self):
    #     if(len(self.stack) <1):
    #         return True
    #     return False

    # def push(self, value):
    #     if(len(self.stack) >= self.maxSize):
    #         self.expand()
    #     self.stack.append(value)

    # def pop(self):
    #     if(len(self.stack) < 1):
    #         return None
    #     return self.stack.pop()

    # def put(self,value_):
    #     if(len(self.stack) > 0):
    #         self.stack.pop()
    #     self.stack.append(value_)
        
    # def peek(self):
    #     if(len(self.stack) <1):
    #         return None
    #     return self.stack[len(self.stack)-1]

    # def expand(self):
    #     self.maxSize *=2

    # def getInOneLine(self):
    #     return " ".join(self.stack)

    # def getSize(self):
    #     return len(self.stack)
    
    # def getCapacity(self):
    #     return self.maxSize
    def __init__(self, size = 10) -> None:
        self.stack = [None] * size
        self.ptrindex = 0
        self.capacity = size
    
    def isEmpty(self) :
        if self.ptrindex == 0 :
            return True
        else :
            return False
    
    def push(self, value) :
        if self.ptrindex == self.capacity :
            return None
        self.stack[self.ptrindex] = value
        self.ptrindex += 1
    
    def pop(self) :
        if self.ptrindex == 0 :
            return None
        pop_value = self.stack[self.ptrindex - 1]
        self.stack[self.ptrindex - 1] = None
        self.ptrindex -= 1
        return pop_value
    
    def put(self,value_) :
        self.stack[self.ptrindex - 1] = value_
    
    def peek(self) :
        return self.stack[self.ptrindex - 1]
    
    def expand(self) :
        l = [None] * self.capacity
        self.stack += l
        self.capacity *= 2
    
    def getInOneLine(self) :
        l = []
        for i in range(self.ptrindex) :
            l.append(self.stack[i])
        return " ".join(l)
    
    def getSize(self) :
        return self.ptrindex
    
    def getCapacity(self) :
        return self.capacity
    
    
class Node():
    def __init__(self, val) -> None :
        self.value = val
        self.next = None
        # self.prev = None
    
class LinkedList():
    def __init__(self) -> None :
        self.head = None
        # self.linklist = {}
        # self.ptrstart = 0
        # self.ptrend = 0
    
    def getList(self) :
        vals_linklist = []
        temp = self.head
        while temp != None :
            vals_linklist.append(temp.value)
            temp = temp.next
        return " ".join(vals_linklist)
        # n = self.linklist[self.ptrstart]
        # for i in range(len(self.linklist)) :
        #     print(n.value , end= ' ')
        #     if self.linklist.get(n.next) != None :
        #         n = self.linklist[n.next]
        # print()
    
    def insertFront(self, new_data) :
        new_node = Node(new_data)
        if(self.head == None):
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        # n = Node(new_data)
        # if len(self.linklist) == 0 :
        #     self.linklist[self.ptrstart] = n
        # else :
        #     n.next = self.ptrstart
        #     self.linklist[self.ptrstart].prev = self.ptrstart - 1
        #     self.ptrstart -= 1
        #     self.linklist[self.ptrstart] = n
    
    def insertEnd(self, new_data) :
        new_node = Node(new_data)
        temp = self.head
        if(temp == None):
            self.head = new_node
            return
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node
        # n = Node(new_data)
        # if len(self.linklist) == 0 :
        #     self.linklist[self.ptrend] = n
        # else :
        #     n.prev = self.ptrend
        #     self.linklist[self.ptrend].next = self.ptrend + 1
        #     self.ptrend += 1
        #     self.linklist[self.ptrend] = n
    
    def reverse(self) :
        perv = None
        if(self.head == None):
            return
        current = self.head
        next = current.next
        while next:
            current.next = perv
            perv = current
            current = next
            if next:
                next = current.next
        current.next = perv
        self.head = current
        # for i in self.linklist :
        #     i.next , i.prev = i.prev , i.next
        # self.ptrstart , self.ptrend = self.ptrend , self.ptrstart
    
classDict = { "stack": Stack, "queue": Queue, "linked_list": LinkedList}

class Utils():
    def __init__(self):
        pass

    def parseLine(self, line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def deleteEndChar(self, line):
        return line.rstrip(line[-1])

    def getAttributePointer(self, object, attribute):
        return getattr(object, attribute)

    def getArgs(self, argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def runFunction(self, attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)    
    
class MainEmu():
    def __init__(self):
        self.utils = Utils()
        self.items = dict()

    def startProgram(self):
        for line in sys.stdin:
            line = self.utils.deleteEndChar(line)
            action, line = self.utils.parseLine(line)
            actionPointer = self.utils.getAttributePointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = self.utils.parseLine(line)
        itemName, line = self.utils.parseLine(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = self.utils.parseLine(line, '.')
        funcName, line = self.utils.parseLine(line, '(')
        argsLine, line = self.utils.parseLine(line, ')')
        args = self.utils.getArgs(argsLine)
        attribute = self.utils.getAttributePointer(self.items[itemName],
                                                   funcName)

        self.utils.runFunction(attribute, args)

if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.startProgram()

# l1 = LinkedList()
# l1.insertFront(2)
# l1.insertEnd(4)
# l1.insertEnd(8)
# l1.insertFront(-3)
# l1.reverse()
# l1.getList()
# q1 = Queue()
# q1.enqueue(1)
# q1.enqueue(2)
# q1.enqueue(3)
# print(q1.isEmpty())
# print(q1.getSize())
# q1.getInOneLine()
# print(q1.dequeue())
# print(q1.dequeue())
# print(q1.dequeue())
# print(q1.isEmpty())
# print(q1.getSize())

# s1 = Stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
# print(s1.isEmpty())
# print(s1.getSize())
# s1.getInOneLine()
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
# print(s1.isEmpty())
# print(s1.getSize())