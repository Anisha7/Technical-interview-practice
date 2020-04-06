# in place reverse linked list methods: O(N) time complexity and O(1) space complexity

def reverseLinkedListRecursive(ll, prev=None, curr=None):
    # initialize parameters to store prev and curr
    if (curr == None and prev == None):
        prev = ll.head
        curr = prev.next
        prev.next = None
    
    # finished reversing whole list
    if (curr == None):
        # since we reversed all points pointing from head towards tail
        # such that they now point from tail towards head
        # we will swap our head and tail variables
        temp = ll.head
        ll.head = ll.tail
        ll.tail = temp
        return
    
    # reverse the pointers between prev and curr
    # initially, prev points to curr
    # we will reverse this so that curr points to prev
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
    return reverseLinkedListRecursive(ll, prev, curr)
    
def reverseLinkedListIterative(ll):
    # initialize parameters to store prev and curr
    prev = ll.head
    curr = prev.next
    prev.next = None
    
    while (curr != None):
        # reverse the pointers between prev and curr
        # initially, prev points to curr
        # we will reverse this so that curr points to prev
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    # finished reversing whole list
    # since we reversed all points pointing from head towards tail
    # such that they now point from tail towards head
    # we will swap our head and tail variables
    temp = ll.head
    ll.head = ll.tail
    ll.tail = temp
    return


# Creating a simple linked list structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, items):
        self.head = Node(items[0])
        self.tail = self.head
        curr = self.head
        for item in items[1:]:
            node = Node(item)
            curr.next = node
            curr = curr.next
            self.tail = curr

# Converts linked list to a list then prints it
def printList(ll):
    curr = ll.head
    reversedArray = []
    while (curr != None):
        reversedArray.append(curr.data)
        curr = curr.next
    print(reversedArray)

# Tests recursive and iterative methods
def test():
    ll = LinkedList([0,1,2,3,4,5])
    print("Testing recursive reverse linked list")
    reverseLinkedListRecursive(ll)
    printList(ll)
    
    ll = LinkedList([0,1,2,3,4,5])
    print("Testing iterative reverse linked list")
    reverseLinkedListIterative(ll)
    printList(ll)
    
test()
    
