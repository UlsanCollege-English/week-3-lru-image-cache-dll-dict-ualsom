class _Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        assert capacity > 0
        self.cap = capacity
        self.map = {}
        # sentinel nodes for doubly linked list
        self.head = _Node("__H__", None)  # most recent after head
        self.tail = _Node("__T__", None)  # least recent before tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        """Add node right after head (mark as most recent)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        # Move accessed node to front (most recent)
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key, val):
        if key in self.map:
            # Update value and move to front
            node = self.map[key]
            node.val = val
            self._remove(node)
            self._add_to_front(node)
        else:
            # Evict least recently used if at capacity
            if len(self.map) == self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.key]
            # Insert new node at front
            new_node = _Node(key, val)
            self._add_to_front(new_node)
            self.map[key] = new_node
