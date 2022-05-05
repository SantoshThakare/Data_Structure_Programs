class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(data, None)
        return

    def insert_values(self, data_list):
        for i in data_list:
            self.insert_at_end(i)
        return

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def is_present(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def remove(self, data):
        temp = self.head
        if self.is_present(data):
            while temp:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    return
                temp = temp.next
        else:
            print(f"{data} is not present")

    def to_string(self):
        temp = self.head
        string_ = " "
        while temp:
            string_ += temp.data + " "
            temp = temp.next
        return string_

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

if __name__ == "__main__":
    link = LinkedList()
    with open("sample.txt", 'r+') as file:
        data_file = file.read()
        file.truncate(0)
    list_file = data_file.split(" ")
    link.insert_values(list_file)
    data = "hello, world"
    present = link.is_present(data)
    if present:
        link.remove(data)
    else:
        link.insert_at_end(data)
    string_ = link.to_string()
    with open("sample.txt", 'w') as file:
        file = open("sample.txt", 'w')
        file.write(string_)