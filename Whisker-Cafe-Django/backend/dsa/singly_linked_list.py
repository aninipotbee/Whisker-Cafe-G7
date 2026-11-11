"""A real singly linked list for the Whisker Cafe visit workflow."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def require_integer(index):
    """Shared input contract; bool is not a usable position."""
    if not isinstance(index, int) or isinstance(index, bool):
        raise TypeError("Index must be an integer.")


class SinglyLinkedList:
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self._size = 0
        if items is not None:
            for value in items:
                self.append(value)

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def insert_at(self, index, value):
        require_integer(index)
        if not 0 <= index <= self._size:
            raise IndexError(index)
        if index == 0:
            self.prepend(value)
            return
        if index == self._size:
            self.append(value)
            return
        previous = self.head
        for _ in range(index - 1):
            previous = previous.next
        node = Node(value)
        node.next = previous.next
        previous.next = node
        self._size += 1

    def remove_at(self, index):
        require_integer(index)
        if not 0 <= index < self._size:
            raise IndexError(index)
        if index == 0:
            removed = self.head
            self.head = removed.next
            self._size -= 1
            if self._size == 0:
                self.tail = None
            removed.next = None
            return removed.data
        previous = self.head
        for _ in range(index - 1):
            previous = previous.next
        removed = previous.next
        previous.next = removed.next
        if removed is self.tail:
            self.tail = previous
        removed.next = None
        self._size -= 1
        return removed.data

    def remove(self, value):
        previous = None
        current = self.head
        while current is not None:
            if current.data == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                if current is self.tail:
                    self.tail = previous
                current.next = None
                self._size -= 1
                if self._size == 0:
                    self.head = self.tail = None
                return True
            previous, current = current, current.next
        return False

    def get(self, index):
        require_integer(index)
        if not 0 <= index < self._size:
            raise IndexError(index)
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def index_of(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values
