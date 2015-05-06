#LRU CACHE USING MIN HEAP INSTEAD OF ORDEREDDICT

import time


class MinHeap(object):
    def __init__(self, l=[]):
        self._heap = []
        if len(l) > 0:
            for e in l:
                self.add(e[0], e[1])

    def _parent(self, i):
        return (i-1)/2

    def _left_child(self, i):
        return 2*i + 1

    def _right_child(self, i):
        return 2*i + 2

    def _is_leaf(self, i):
        return self._left_child(i) >= len(self._heap) and self._right_child(i) >= len(self._heap)

    def _one_child(self, i):
        return self._left_child(i) < len(self._heap) and self._right_child(i) >= len(self._heap)

    def _down_heapify(self, i):
        if self._is_leaf(i):
            return self._heap

        if self._one_child(i):
            if self._heap[self._left_child(i)][1] < self._heap[i][1]:
                self._heap[self._left_child(i)], self._heap[i] = self._heap[i], self._heap[self._left_child(i)]
            return self._heap

        if min(self._heap[self._left_child(i)][1], self._heap[self._right_child(i)][1]) >= self._heap[i][1]:
            return self._heap

        if self._heap[self._left_child(i)][1] < self._heap[self._right_child(i)][1]:
            self._heap[self._left_child(i)], self._heap[i] = self._heap[i], self._heap[self._left_child(i)]
            self._down_heapify(self._left_child(i))
            return self._heap

        self._heap[self._right_child(i)], self._heap[i] = self._heap[i], self._heap[self._right_child(i)]
        self._down_heapify(self._right_child(i))
        return self._heap

    def _up_heapify(self, i):
        if self._parent(i) >= 0:
            if self._heap[self._parent(i)][1] > self._heap[i][1]:
                self._heap[self._parent(i)], self._heap[i] = self._heap[i], self._heap[self._parent(i)]
                self._up_heapify(self._parent(i))
                return self._heap
        return self._heap

    def validate_heap(self):
        for i, e in enumerate(self._heap):
            if self._parent(i) >= 0:
                if self._heap[self._parent(i)][1] > self._heap[i][1]:
                    print self._heap[self._parent(i)], self._heap[i]
                    return False
        return True

    def add(self, key, value):
        self._heap.append((key, value))
        self._up_heapify(len(self._heap) - 1)

    def pop(self):
        min_value = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._down_heapify(0)
        return min_value

    def update(self, key, value):
        for i, e in enumerate(self._heap):
            if e[0] == key:
                self._heap[i] = (key, value)
                if value > e[1]:
                    self._down_heapify(i)
                else:
                    self._up_heapify(i)
                return self._heap
        return self._heap

    def delete(self, key):
        for i, e in enumerate(self._heap):
            if e[0] == key:
                last_element = self._heap.pop()
                self._heap[i] = last_element
                self._down_heapify(i)
                return self._heap
        return self._heap


class LRUCache(object):
    def __init__(self, capacity):
        self._cache_dict = {}
        self._cache_heap = MinHeap()
        self._capacity = capacity

    def _is_in_cache(self, key):
        if self._cache_dict.get(key):
            return True
        return False

    def _is_over_capacity(self):
        if len(self._cache_dict) >= self._capacity:
            return True
        return False

    def set(self, key, value):
        new_time = time.time()

        if self._is_in_cache(key):
            self._cache_heap.update(key, new_time)
            self._cache_dict[key] = (value, new_time)
            return self._cache_dict

        if self._is_over_capacity():
            min_value = self._cache_heap.pop()[0]
            del self._cache_dict[min_value]

        self._cache_heap.add(key, new_time)
        self._cache_dict[key] = (value, new_time)
        return self._cache_dict

    def get(self, key):
        if not self._is_in_cache(key): 
            raise KeyError("this key is not in the cache")
        
        new_time = time.time()
        self._cache_heap.update(key, new_time)
        value = self._cache_dict[key][0]
        self._cache_dict[key] = (value, new_time)
        return value

    def get_lru_el(self):
        key = self._cache_heap._heap[0][0]
        return self._cache_dict[key]

    def get_dict(self):
        return self._cache_dict


lru_cache = LRUCache(3)

lru_cache.set("user1", "teme")
lru_cache.set("user2", "oge")
lru_cache.set("user3", "dzenan")
lru_cache.set("user4", "francis")
lru_cache.set("user5", "baba")

lru_cache.get("user3")
lru_cache.get("user4")

lru_cache.set("user2", "oge")
lru_cache.set("user6", "tommy")

print lru_cache.get_dict()
print lru_cache.get_lru_el()

        
            


