class HashMap:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        h = h % self.max
        return h

    # def add(self, key, value):
    #     h = self.get_hash(key)
    #     self.arr[h] = value
    # A better way to do the same. (Use only one function at a time)

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]
    # A better way to do the same. (Use only one function at a time)

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    # def remove(self, key):
    #     h = self.get_hash(key)
    #     self.arr[h] = None
    # A better way to do the same. (Use only one function at a time)

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    t = HashMap()
    # t.add('march 4', 850)
    # t.add('march 15', 100)
    # t.add('march 20', 120)
    t['march 20'] = 120
    t['march 15'] = 100
    t['march 4'] = 850
    t['april 5'] = 650
    # t.remove('march 4')
    del t['march 4']
    print(t['march 15'])
    print(t['april 5'])
