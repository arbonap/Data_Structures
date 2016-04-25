from test import testEqual
class Stack:
    """LIFO array where top is the end of list"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """Returns boolean to check if stack is empty"""
        return self.items == []

    def push(self, item):
        """Appends to top of stack (end of list)"""
        return self.items.append(item)

    # def push(self, item):
    # """ Inserts to top of stack (start of list) """
        # return self.items.insert(0, item)

    def pop(self):
        """Deletes from the top of the stack"""
        return self.items.pop()

    # def pop(self):
    # """Deletes from the top of the stack (start of list)"""
    #return self.items.pop(0)

    def peek(self):
        """Returns last / top item of stack (doesn't do anything to it)"""
        return self.items[len(self.items)-1]

    # def peek(self):
    # """Returns from the top of the stack (start of list)"""
    #     return self.items[0]

    def size(self):
        return len(self.items)

#reverse a string using a Stack
#create stack
#loop over chars, pushing them out one at a time
#while not is empty
#pop them off and concatenate them into empty string


def revstring(mystr):
    myStack = Stack()

    for char in str:
        myStack.push(char)

    revstr = ""

    while not myStack.isEmpty():
        revstr += myStack.pop()

    return revstr


