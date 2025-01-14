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

    def insert_values(self, data):
        for item in data:
            self.insert_at_end(item)

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

    def get_length(self):
        itr = self.head
        count = 1
        while itr.next:
            itr = itr.next
            count +=1
        return count

    def remove_at(self, index):
        itr = self.head
        if index == 0:
            self.head = self.head.next

        if index<0 or index > self.get_length():
            raise Exception("! Invalid Index !")
        
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

if __name__=='__main__':
    l1 = linked_list()
    l1.insert_values([1,2,3,4])
    print(l1.get_length())
    l1.remove_at(2)
    l1.print()
   

        