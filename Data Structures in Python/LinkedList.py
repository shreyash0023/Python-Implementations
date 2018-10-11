#LINKED LIST IMPLEMENTATION

class Node:
    def __init__(self,data=None):
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        trav = self.head
        x = []
        while trav.next != None:
            trav= trav.next
            x.append(trav.data)
        print x

    def length(self):
        cur = self.head
        i=0
        while cur.next != None:
            i+=1
            cur=cur.next
        return i

    def at_idx(self,idx):
        if idx >= self.length():
            print 'ERROR IN ARGUMENT'
        i=0
        cur = self.head
        while True:
            if(i==idx):
                print cur.data
                print 'Item number in the list = '
                print i
                print 'Data in the node = '
                print cur.data
                return cur.data
            cur=cur.next
            i+=1

    def test(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        print cur
        print cur.next
        print cur.data




list = LinkedList()

for x in range(0,11):
    list.append(x)


list.display()
print list.length()
list.at_idx(3)

print '\n'
list.test()
