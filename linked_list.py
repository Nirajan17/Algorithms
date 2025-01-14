# creating linked list in python 

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def print(self):
        if self.head == None:
            print("Linked list is empty")
            return
        
        itr = self.head
        ll1 = ' '
        while itr:
            ll1 += str(itr.data) + " "
            itr = itr.next
        
        print(ll1)

if __name__=='__main__':
    l1 = linked_list()
    l1.insert_at_begin(10)
    l1.insert_at_begin("lecturer")
    l1.insert_at_end(3)
    l1.insert_at_begin(2)
    l1.insert_at_end("Nirajan")
    l1.print()
   

        