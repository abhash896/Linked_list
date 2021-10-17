class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, list_of_data):
        self.head = None
        for i in list_of_data:
            self.insert_at_end(i)
        return

    def length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count +=1
        return count

    def remove_at(self, index):
        if index < 0 or index > self.length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # since itr has address of the next node, it should be stored in the new node and its values should be changed to the new node's address.
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    l = LinkedList()
    l.insert_at_beginning(8)
    l.insert_at_beginning(98)
    l.insert_at_beginning(2)
    l.insert_at_end(68)
    l.insert_values(['banana', 'mango', 'apple', 'grapes'])
    l.print()
    print(f'The length of this linked list is : {l.length()}')
    l.remove_at(2)
    l.insert_at(2, 'strawberry')
    l.insert_at(0, 'blueberries')
    l.print()
    print(f'The length of this linked list is : {l.length()}')
    l.insert_after_value('strawberry', 'avocado')
    l.remove_by_value('grapes')
    l.remove_by_value("banana")

    l.print()
