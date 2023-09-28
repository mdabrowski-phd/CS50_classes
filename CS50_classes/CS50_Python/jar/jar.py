class Jar:

    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, amount):
        if amount + self.size > self.capacity:
            raise ValueError
        self._size += amount

    def withdraw(self, amount):
        if amount > self.size:
            raise ValueError
        self._size -= amount

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
