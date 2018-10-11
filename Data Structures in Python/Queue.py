#Queue Implementation with Linked List

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue_List:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

    def length(self):
        if self.head.next == None:
            print 'EMPTY QUEUE'
            return
        cur = self.head
        i=0
        while cur.next != None:
            i+=1
            cur=cur.next
        return i

    def isEmpty(self):
        return self.length() == 0

    def enQueue(self,data):
        new_node = Node(data)
        if self.head.next == None:
            self.head.next = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
        #q1.test()

    def deQueue(self):
        if self.head.next == None:
            print 'CANNOT DEQUE. QUEUE EMPTY!'
            return
        if self.length() == 1:
            del self.head.next
            self.head.next = None
            self.tail.next = None
            return
        cur = self.head.next
        while cur.next.next != None:
            cur = cur.next
        print cur.data
        del cur.next

        self.tail.next = cur
        self.tail.next.next = None


    def display_from_tail(self):
        cur = self.tail
        x = []
        while cur.next != None:
            x.append(cur.data)
            cur = cur.next
        return x

    def display_from_head(self):
        cur = self.head.next
        x = []
        #print self.head.data
        while cur != None:
            x.append(cur.data)
            cur = cur.next
        return x

    def test1(self):
        print '\n'
        print self.head.next.data
        print self.tail.next.data
        print self.head
        print self.tail
        print self.head.next
        print self.tail.next
        print '\n'

    def test2(self):
        print self.head
        print self.tail
        print self.head.next
        print self.tail.next
q1 = Queue_List()


for x in range(0,5):
    q1.enQueue(x)

print q1.display_from_head()
print q1.display_from_tail()
q1.deQueue()

#print q1.display_from_head()
q1.deQueue()
q1.deQueue()
#print q1.display_from_head()
q1.deQueue()
q1.deQueue()
#q1.test2()
q1.length()
q1.deQueue()


for x in range(0,5):
    q1.enQueue(x)

print q1.display_from_head()
print q1.display_from_tail()

#print q1.length()
#print q1.display_from_head()
#print q1.display_from_head()   #printing from head -> should give all the queue elements
#q1.deQueue()
#print q1.display_from_head()
