# Data Structure Explanation for Whisker Café

## FIFO visitor queue

Whisker Café uses a queue to manage visitors waiting for a cat lounge session. A queue follows First In, First Out (FIFO), which means the first visitor who joins is the first visitor welcomed. The `ServiceQueue` class uses Python's `collections.deque` so it can add a reservation at the rear with `enqueue()` and remove the earliest reservation from the front with `dequeue()`. The `peek()` method checks who is next without removing that reservation. Both adding and removing take O(1) time because deque is designed for efficient operations at either end. The `to_list()` method creates a new list in arrival order so Django can save the queue state and rebuild it on the next page request. An empty queue raises `IndexError` when `dequeue()` or `peek()` is called.

## Singly linked list visit workflow

The visit workflow is stored as a singly linked list. Each `Node` contains a value in `data` and a reference to the next node in `next`. The list has a `head` reference for the first node, a `tail` reference for the last node, and a cached `_size` value for the number of nodes. When a new visit stage is appended, the current tail's `next` reference points to the new node and `tail` is updated. This is O(1) because the list already knows its last node. The `get()` operation is O(n) because a singly linked list cannot jump directly to an index. It must start at `head` and follow each `next` reference until it reaches the requested position. Inserting or removing at a middle position is also O(n) because the previous node must first be found. The final node always has `next = None`, so the structure is not circular.
