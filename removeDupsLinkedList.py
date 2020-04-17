# removing duplicates from a linked list
# Ideas: Go through linked list, and track what data we already saw
        # if we saw it already, remove it

# 1 -> 2 -> 3 -> 4
# delete 3
# node2.next.data == 3 (true)
# node2.next = node2.next.next

# Pseudocode
    # Initialize seen tracker: set
    # Initialize currNode as head + add to set
    # Iterate through linked list
        # Check if data (currNode.next.data) is in set
            # delete the next node: currNode.next = currNode.next.next
        # else:
            # append to set

def removeDupsFromLinkedList(L):
    if L.head == None:
        return 
    tracker = set()
    currentNode = L.head
    tracker.add(currentNode.data)
    
    while currentNode.next != None:
        if currentNode.next.data in tracker:
            currentNode.next = currentNode.next.next
        else:
            tracker.add(currentNode.next.data)
            currentNode = currentNode.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, items):
        self.head = None
        self.tail = None
        for item in items:
            self.add(item)
     
    def add(self, item):
        if (self.head == None):
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def printItems(self):
        curr = self.head
        data = []
        while curr != None:
            data.append(curr.data)
            curr = curr.next
        return data

LL = LinkedList([1,2,2,3,4,4,5])
print(LL.printItems())
removeDupsFromLinkedList(LL)
print(LL.printItems())

