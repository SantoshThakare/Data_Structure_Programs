"""
whatever goes last comes out first
"""
class Stack(object):
    def __init__(self):
        self.item =[]
    def push(self,item=''):
        """
        push the element at the last index
        return: none
        """
        self.item.append(item)
    def pop(self):
        """
        this will remove last item
        return: none
        """
        self.item.pop()
        pass
    def peek(self):
        """
        Allows us to see the last elements
        :return: last item
        """
        if self.item:
            return self.item[-1]
        else:
            return None

    def size(self):

        if self.item:
            return len(self.item)
        else:
            return None

    def isempty(self):
        """
        tells whether the stack is empty or not
        :return :  bool value
        """
        if self.item == []:
            return True
        else:
            return False

if __name__ == '__main__':
    stack = Stack()
    stack.push("1")
    stack.push("2")
    stack.push("3")
    print(stack.size())
    print(stack.peek())

    stack.pop()
    print(stack.size())
    print(stack.peek())
    print(stack.isempty())
    stack.pop()
    print(stack.isempty())
    stack.pop()
    print(stack.isempty())

