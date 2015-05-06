import unittest
from nose.tools import raises

from lru_cache import LRUCache

class LRUCacheTests(unittest.TestCase):
    def setUp(self):
        self.lru_cache = LRUCache(3)
        self.lru_cache.set('user1', 'timur')
        self.lru_cache.set('user2', 'ogden')
        self.lru_cache.set('user3', 'francis')
        self.lru_cache.set('user4', 'amra')

    def tearDown(self):
        self.lru_cache = None

    @raises(KeyError)
    def test_key_error(self):
        """
        First element should be removed from cache
        """
        self.lru_cache.get('user1')

    def test_get(self):
        """
        Checks to see if 3 most recent elements are in the cache
        """
        self.assertTrue(self.lru_cache.get('user2') == 'ogden')
        self.assertTrue(self.lru_cache.get('user3') == 'francis')
        self.assertTrue(self.lru_cache.get('user4') == 'amra')

    @raises(KeyError)
    def test_lru_get_and_set(self):
        """
        Performs a few get and set operations: user3 should be the least recently used element and should raise a key error. 
        user2, user 4 and user5 should still be in the cache
        """
        self.lru_cache.get('user2')
        self.lru_cache.set('user5', 'tom')
        
        self.assertTrue(self.lru_cache.get('user2') == 'ogden')
        self.assertTrue(self.lru_cache.get('user4') == 'amra')
        self.assertTrue(self.lru_cache.get('user5') == 'tom')

        self.lru_cache.get('user3')

    @raises(KeyError)
    def test_update(self):
        """
        Updates user2 before adding new element. user4 should be the lru element and user3 should be removed from cache.
        """
        self.lru_cache.set('user2', 'Ogden')
        self.lru_cache.set('user5', 'tom')

        self.assertTrue(self.lru_cache.get('user2') == 'Ogden')
        self.assertFalse(self.lru_cache.get('user2') == 'ogden')

        self.assertTrue(self.lru_cache.get_lru_el() == 'user4')
        self.lru_cache.get('user3')


