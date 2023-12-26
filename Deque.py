class Deque:
    __lengths = [5, 11, 23, 47, 97, 397, 797, 1597, 3203, 6421, 12853, 25717, 51437, 102877, 205759, 411527, 823117,
                 1646237, 3292489, 6584983, 13169977, 26339969, 52679969, 105359939, 210719881, 421439783]

    def __init__(self, seq=None):
        self.length = 0
        self.count = 0
        self.start = None
        self.new_deque = None
        self.deque = [None for _ in range(self.__lengths[self.length])]
        self.left, self.right = len(self.deque) // 2 + 1, len(self.deque) // 2
        if seq:
            for value in seq:
                self.append(value)

    def __contains__(self, item):
        if item is not None:
            return item in self.deque

    def __len__(self):
        return self.count

    def __iter__(self):
        for item in self.deque:
            if item is not None:
                yield item

    def __repr__(self):
        result = [item for item in self.deque if item is not None]
        return result.__repr__()

    def __str__(self):
        result = [item for item in self.deque if item is not None]
        return result.__str__()

    def append(self, value):
        if self.right + 1 < len(self.deque):
            self.count += 1
            self.right += 1
            self.deque[self.right] = value
        else:
            self.count += 1
            self.length += 1
            self.new_deque = [None for _ in range(self.__lengths[self.length])]
            self.start = len(self.new_deque) // 2 - (self.count // 2)
            for index in range(self.left, self.right + 1):
                self.new_deque[self.start] = self.deque[index]
                self.start += 1
            self.right = self.start
            self.left = self.right - self.count + 1
            self.new_deque[self.start] = value
            self.deque = self.new_deque
            self.new_deque, self.start = None, None

    def append_left(self, value):
        if self.left - 1 >= 0:
            self.count += 1
            self.left -= 1
            self.deque[self.left] = value
        else:
            self.count += 1
            self.length += 1
            self.new_deque = [None for _ in range(self.__lengths[self.length])]
            self.start = len(self.new_deque) // 2 - (self.count // 2)
            self.new_deque[self.start - 1] = value
            for index in range(self.left, self.right + 1):
                self.new_deque[self.start] = self.deque[index]
                self.start += 1
            self.right = self.start - 1
            self.left = self.right - self.count + 1
            self.deque = self.new_deque
            self.new_deque, self.start = None, None

    def pop(self):
        if not self.count:
            return
        result = self.deque[self.right]
        self.deque[self.right] = None
        self.right -= 1
        self.count -= 1
        return result

    def popleft(self):
        if not self.count:
            return
        result = self.deque[self.left]
        self.deque[self.left] = None
        self.left += 1
        self.count -= 1
        return result

    @property
    def get_left(self):
        if self.deque[self.left] is not None:
            return self.deque[self.left]
        return self.deque[self.right - self.count + 1]

    @property
    def get_right(self):
        if self.deque[self.right] is not None:
            return self.deque[self.right]
        return self.deque[self.left + self.count - 1]
