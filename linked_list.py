# -*- encoding: utf-8 -*-

class Node:
    """
    A class for storing a singly linked list node
    Models two attributes – data and the next node in the linked list
    """
    data = None
    next = None
    def __init__(self, data=None):
        self.data = data

    def __repr__(self):
        return "{ Node data: %s -> next: %s }" % (self.data, self.next.data if self.next else None)

class SinglyLinkedList:
    """
    Singly linked list
    """
    head = None
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next

        return ' -> '.join(nodes)

    def is_empty(self):
        return self.head == None

    def prepend(self, first_node):
        """
        Adds a new node to the head of the list
        Takes O(1) time
        """
        first_node.next = self.head
        self.head = first_node

    def size(self):
        """
        Returns the length of the list
        Takes O(n) time (Linear Time)
        """
        current = self.head
        total_size = 0
        while current != None:
            total_size += 1
            current = current.next
        return total_size

    def search(self, key):
        """
        Search for the first node containing the date of the key
        Returns the node or None if not found
        Takes O(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def insert(self, new_node, position):
        """
        Inserts a node in the position of your choice or at the end if it exceeds the size of it
        Insertion takes O(1) time
        Finding the node takes O(n) time
        That's why the overal performance is O(n)
        """
        if position == 0:
            self.prepend(new_node)

        if position >= self.size():
            position = self.size()

        previous_node = self.head
        next_node = previous_node.next
        for i in range(position + 1):
            if i == 0: continue

            if i == position:
                previous_node.next = new_node
                new_node.next = next_node
                break
            previous_node = next_node
            next_node = next_node.next

    def delete(self, data):
        """
        Deletes the first node that finds with the selected data or None if not found
        Takes O(n) overall because finding the node to delete is a Linear Time operation
        """
        previous_node = None
        current_node = self.head
        next_node = current_node.next
        for i in range(self.size()):
            if self.head.data == data:
                if self.head.next != None:
                    self.head = next_node
                else:
                    self.head = None
                break
            elif current_node.data == data:
                previous_node.next = next_node
                break
            previous_node = current_node
            current_node = next_node
            next_node = current_node.next

N1 = Node(10)
N2 = Node(20)
N3 = Node(30)
N4 = Node(40)
N5 = Node(50)

list = SinglyLinkedList(N1)
list.prepend(N2)
list.prepend(N3)
