class HashMaping:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, num):
        return num % 11

    def add_num(self, data):
        index = self.get_hash(data)
        self.arr[index].append(data)
        self.arr[index].sort()

    def remove(self, data):
        for i in self.arr:
            for j in i:
                if data == j:
                    i.remove(j)
                    return True
        return False

    def value_list(self):
        list_ = []
        for i in self.arr:
            for j in i:
                list_.append(j)
        return list_

    def display_hash(self):
        for i in self.arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    hash_obj = HashMaping()
    input_list = [3, 8, 12, 20, 28, 38, 42]

    for i in input_list:
        hash_obj.add_num(i)

    hash_obj.display_hash()
    in_num = 42
    check = hash_obj.remove(in_num)
    if not check:
        hash_obj.add_num(in_num)
    hash_obj.display_hash()

    out_list = hash_obj.value_list()
    print(out_list)