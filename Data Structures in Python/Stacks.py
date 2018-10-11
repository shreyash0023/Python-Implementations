class Node:
    def __init__(self,data=None):
        self.next = None
        self.data = data

class Stacks:
    def __init__(self):
        self.head = Node()
        self.base = Node()

    def size(self):
        if self.head.next == None:
            return 0
        cur = self.base
        i=0
        while cur.next != None:
            cur = cur.next
            i+=1
        return i

    def push(self,data):
        new_node = Node(data)
        if self.size() == 0:
            self.head.next = new_node
            self.base.next = new_node

        else:
            self.head.next.next= new_node
            self.head.next = new_node

    def pop(self):
        if self.size() == 0:
            print 'EMPTY STACK'
            return
        else:
            cur = self.base
            while cur.next!= self.head.next:
                cur = cur.next
            del self.head.next
            cur.next = None
            self.head.next = cur
            print self.size()


    def current_element(self):
        if self.head.next == None:
            return
        return self.head.next.data

    def print_stack(self):
        cur = self.base.next
        x = []
        while cur != None:
            x.append(cur.data)
            cur = cur.next
        return x

s1 = Stacks()

for x in range(0,5):
    s1.push(x)

#print s1.size()
print s1.print_stack()

s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
print s1.print_stack()

for x in range(5,15):
    s1.push(x)
print s1.print_stack()