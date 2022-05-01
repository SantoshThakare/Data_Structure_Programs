class Stack(object):
    def __init__(self):
        self.values = []

    def push(self, value):

        self.values.append(value)

    def pop(self):

        return self.values.pop()

class Queue(object):
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop(0)

stack = Stack()

queue = Queue()

class PalindromeChecker(object):
    def __init__(self, word):
        self.word = word
        self.queue = Queue()
        self.stack = Stack()

    def check_palindrome(self):
        for letter in self.word:
            self.queue.push(letter)
            self.stack.push(letter)
        for i in range(len(self.word)):
            if self.queue.pop() != self.stack.pop():
                return False
        return True

if __name__ == '__main__':
    str = input("Enter the String: ")
    res = PalindromeChecker(str)
    if res.check_palindrome():
        print(str, " is a palindrome")
    else:
        print(str, " is not a palindrome")