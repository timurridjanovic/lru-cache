import unittest
from nose.tools import raises

from lru_cache import LRUCache

class LRUCacheScaleTests(unittest.TestCase):
    def setUp(self):
        self.capacity = 5000000
        self.__num_over_capacity = 500002
        self.lru_cache = LRUCache(self.capacity)
        
        for i in xrange(1, self.capacity + self.__num_over_capacity):
            self.lru_cache.set('user' + str(i), 'user_number_' + str(i))

    def tearDown(self):
        self.lru_cache = None

    @raises(KeyError)
    def test_set_and_get(self):
        """
        lru element should be user2 and user1 sould be removed.
        """
        self.assertEqual(self.lru_cache.get_lru_el(), 'user' + str(self.__num_over_capacity))
        self.lru_cache.get('user' + str(self.__num_over_capacity - 1))

    def test_update(self):
        """
        test update
        """
        self.lru_cache.set('user' + str(self.__num_over_capacity + self.capacity/2), 'ANON_USER')
        self.assertTrue(self.lru_cache.get('user' + str(self.__num_over_capacity + self.capacity/2)) == 'ANON_USER')

        self.lru_cache.set('user' + str(self.__num_over_capacity), 'USER' + str(self.__num_over_capacity))
        self.assertEqual(self.lru_cache.get_lru_el(), 'user' + str(self.__num_over_capacity + 1))


