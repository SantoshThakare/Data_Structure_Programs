class Stack:
    def __init__(self):
        self.container = []

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def display(self):
        return print(self.container)

stack = Stack()

open_list = ['[', '{', '(']
close_list = [']', '}', ')']

def is_balance(string):
    for i in string:
        if i in open_list:
            stack.push(i)
        if i in close_list:
            position = close_list.index(i)
            if stack.size() > 0 and open_list[position] == stack.peek():
                stack.pop()
            else:
                return "Unbalanced"

    if stack.size() == 0:
        return "Balanced"

    else:
        return "Unbalanced"


if __name__ == '__main__':
    input_string = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"
    print(is_balance(input_string))