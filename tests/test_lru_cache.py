from src.lru_cache import LRUCache

def test_put_get_evict_order():
    c = LRUCache(2)
    c.put("A", 1)
    c.put("B", 2)
    assert c.get("A") == 1   # A becomes most recent
    c.put("C", 3)            # evicts least recent: B
    assert c.get("B") == -1  # changed to expect -1
    assert c.get("A") == 1
    assert c.get("C") == 3
    c.put("D", 4)            # evicts least recent: A
    assert c.get("A") == -1 and c.get("D") == 4

def test_update_existing_key():
    c = LRUCache(2)
    c.put("A", 1)
    c.put("B", 2)
    c.put("A", 10)           # Update A's value and move to front
    assert c.get("A") == 10
    c.put("C", 3)            # Evicts B
    assert c.get("B") == -1
    assert c.get("C") == 3

def test_capacity_one():
    c = LRUCache(1)
    c.put("X", 100)
    assert c.get("X") == 100
    c.put("Y", 200)
    assert c.get("X") == -1  # X evicted
    assert c.get("Y") == 200
