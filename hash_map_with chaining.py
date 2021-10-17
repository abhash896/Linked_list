class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        h = h % self.max
        return h

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        flag = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                flag = True

        if not flag:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


if __name__ == '__main__':
    t = HashTable()
    t['march 5'] = 310
    t['march 6'] = 421
    t['march 7'] = 68
    t['march 8'] = 56472
    t['march 17'] = 85
    print(t.arr)

