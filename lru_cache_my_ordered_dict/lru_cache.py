
#LRU CACHE USING OWN IMPLEMENTATION OF ORDEREDDICT

class OrderedDict(object):
    def __init__(self):
        self.__dict = {}
        self.__map = {}
        self.__end = None
        self.__first = None

    def __str__(self):
        return str(self.__dict)

    def __getitem__(self, key):
        return self.__dict[key]

    def __setitem__(self, key, value):
        if self._is_first_element():
            self._store_first_element(key, value)
        else:
            self._store_element(key, value)
    
    def __delitem__(self, key):
        if not self.__map.get(key):
            return

        if self.__first == key:
            self.pop(last=False)
            return

        if self.__end == key:
            old_end = self.__end
            new_end = self.__map[old_end][0]
            self.__map[new_end][2] = None
            self._delete_from_dicts(key)
            self.__end = new_end
            return

        node = self.__map[key]
        prev = node[0]
        next = node[2]
        self.__map[prev][2] = next
        self.__map[next][0] = prev
        self._delete_from_dicts(key)
        return

    def __iter__(self):
        curr = self.__first
        while curr != None:
            node = self.__map[curr]
            next = node[2]
            yield curr
            curr = next

    def __len__(self):
        return len(self.__dict)

    
    def _is_first_element(self):
        if not self.__end:
            return True
        return False

    def _delete_from_dicts(self, key):
        del self.__map[key]
        del self.__dict[key]

    def _store_first_element(self, key, value):
        self.__dict[key] = value
        self.__map[key] = [None, value, None]
        self.__end = key
        self.__first = key

    def _store_element(self, key, value):
        if not self.__map.get(key):
            prev = self.__end
            self.__map[prev][2] = key
            self.__map[key] = [prev, value, None]
            self.__dict[key] = value
            self.__end = key
            return

        self.__map[key][1] = value
        self.__dict[key] = value
        return

    def pop(self, last=True):
        if last:
            old_last = self.__end
            old_last_value = self.__map[old_last][1]
            new_last = self.__map[old_last][0]
            self._delete_from_dicts(old_last)
            self.__map[new_last][2] = None
            self.__end = new_last
            return old_last_value

        old_first = self.__first
        old_first_value = self.__map[old_first][1]
        new_first = self.__map[old_first][2]
        self._delete_from_dicts(old_first)
        self.__map[new_first][0] = None
        self.__first = new_first
        return old_first_value

    def keys(self):
        l = []
        for e in self:
            l.append(e)
        return l

    def get(self, key):
        return self.__dict.get(key)



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
            self._cache_dict.pop(last=False)
        
        self._cache_dict[key] = value
        return self._cache_dict


    def get(self, key):
        if not self._is_in_cache(key): 
            raise KeyError("this key is not in the cache")
        
        value = self._cache_dict[key]
        self.set(key, value)
        return value

    def get_lru_el(self):
        return self._cache_dict._OrderedDict__first

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

