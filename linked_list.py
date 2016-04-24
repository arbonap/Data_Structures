#Create a Linked_list Class


class Node:

    def __init__(self, initdata):
        # nodes consist of data and a next pointer
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        # Creates a new node and places item as its data
        temp.setNext(self.head)
        #Changes the next references of the new node to refer to the old first node of the list
        self.head = temp

    def size(self):
        current_node = self.head
        count = 0

        while current_node is not None:
            current_node += 1
            current_node.getNext()

        return count

    def search(self, item):
        current_node = self.head
        found = False

        while current_node is not None and found is False:
            if current_node.getData() == item:
                found = True
            else:
                current_node = current_node.getNext()

            return found
