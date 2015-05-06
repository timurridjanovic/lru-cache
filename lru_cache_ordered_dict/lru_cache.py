
#LRU CACHE USING OWN IMPLEMENTATION OF ORDEREDDICT

from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self._cache_dict = OrderedDict()
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
        if self._is_in_cache(key):
            del self._cache_dict[key]
            self._cache_dict[key] = value
            return self._cache_dict

        if self._is_over_capacity():
            self._cache_dict.popitem(last=False)
        
        self._cache_dict[key] = value
        return self._cache_dict


    def get(self, key):
        if not self._is_in_cache(key): 
            raise KeyError("this key is not in the cache")
        
        value = self._cache_dict[key]
        self.set(key, value)
        return value

    def get_lru_el(self):
        return next(iter(self._cache_dict))

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

