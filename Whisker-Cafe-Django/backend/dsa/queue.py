"""FIFO service queue used by the Whisker Cafe visitor waiting line."""
from collections import deque


class ServiceQueue:
    def __init__(self, items=None):
        # deque preserves arrival order and supports O(1) operations at both ends.
        self._items = deque(items if items is not None else ())

    def enqueue(self, value):
        """Add a visitor/request at the rear of the line in O(1)."""
        self._items.append(value)

    def dequeue(self):
        """Remove and return the earliest waiting visitor in O(1)."""
        if self.is_empty():
            raise IndexError("The service queue is empty.")
        return self._items.popleft()

    def peek(self):
        """Return the next visitor without removing them."""
        if self.is_empty():
            raise IndexError("The service queue is empty.")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def to_list(self):
        """Return a new arrival-order snapshot, from front to rear."""
        return list(self._items)
