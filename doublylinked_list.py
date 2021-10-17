class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class doublylinked_list:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node

        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node  # Updating the head node with the node we are adding at the beginning.

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)


    def print_forward(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.next
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        if self.head is None:
            print('Linked list is empty')
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.prev
        print(llstr)

    def insert_values(self, list_of_data):
        self.head = None
        for i in list_of_data:
            self.insert_at_end(i)
        return

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next, itr)
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                if itr.next.next is None:
                    itr.next = None
                elif itr.next.next is not None:
                    itr.next = itr.next.next
                    itr.next.prev = itr

                break
            itr = itr.next
            count += 1





if __name__ == '__main__':
    l = doublylinked_list()
    l.insert_at_beginning(25)
    l.insert_at_beginning(30)
    l.print_forward()
    l.print_backward()
    l.insert_values(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    l.print_forward()
    l. insert_at(2, 'abhash')
    l.print_forward()
    l.remove_at(3)
    l.print_forward()
    l.print_backward()
