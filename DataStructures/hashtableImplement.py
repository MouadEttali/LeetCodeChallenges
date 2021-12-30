class hashmap:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __getitem__(self,index):
        return self.arr[self.get_hash(index)]

    def __setitem__(self,key,val):
        self.arr[self.get_hash(key)]= val


if __name__ == '__main__':
    t = hashmap()
    t['Jan 9'] = 36
    t['Jan 4'] = 31
    print(t['Jan 9'])
