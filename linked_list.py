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

    def remove(self, item):
        current_node = self.head
        previous = None #provding us with node whose next reference must be changed
        found = False

        while found is False:
            if current_node.getData() == item:
                found = True
            else:
                #inch-worming:
                #previous catches up to current
                #before current moves ahead
                previous = current_node
                current_node = current_node.getNext()
        #special-case when item to be removed happens
        #to be the head (when found is True and previous is None)
        if previous is None:
            self.head = current_node.getNext()
        else:
            #node to be removed somwhere down the LL structure
            previous.setNext(current_node.getNext())
