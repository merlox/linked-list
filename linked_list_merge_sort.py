from linked_list import Node, SinglyLinkedList

def merge_sort(list):
    '''
    Splits the linked list into halves and sorts them recursively
    Takes O(kn log n) runtime because you are splitting repeatedly and merging with loops
    '''

    # The last element is a single node, we know that because it doesn't contain a next node
    if list.size() <= 1 or list.head is None:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    '''
    Splits a linked list into two new ones right in the middle or None in the right if it has 1 node only
    '''
    left = SinglyLinkedList()
    right = SinglyLinkedList()

    if list is None or list.head is None:
        left = list
        right = None
    else:
        mid_point = list.size() // 2
        mid_node = list.node_at_index(mid_point - 1)
        left = list
        right.head = mid_node.next
        mid_node.next = None
    return left, right

def merge(a, b):
    '''
    Merges two linked list sorting data in the nodes
    Returns a list_merged linked list
    '''
    list_merged = SinglyLinkedList()
    list_merged.prepend(Node(0)) # Add a fake head that is discarted later to avoid empty lists
    current = list_merged.head
    a_head = a.head
    b_head = b.head

    # Iterate over each node until we reach the tail one and build the list by updating the current next node
    while a_head != None or b_head != None:
        if a_head is None:
            current.next = b_head
            b_head = b_head.next
        elif b_head is None:
            current.next = a_head
            a_head = a_head.next
        else:
            if a_head.data < b_head.data:
                current.next = a_head
                a_head = a_head.next
            else:
                current.next = b_head
                b_head = b_head.next
        current = current.next


    # Discard fake head and set first list_merged node as head
    list_merged.head = list_merged.head.next
    return list_merged


N1 = Node(10)
N2 = Node(20)
N3 = Node(30)
N4 = Node(40)
N5 = Node(50)
list = SinglyLinkedList(N1)
list.prepend(N2)
list.prepend(N3)
list.prepend(N4)
list.prepend(N5)

print('Original', list)
print('Sorted', merge_sort(list))
