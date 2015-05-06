import unittest
from nose.tools import raises

from lru_cache import LRUCache

class LRUCacheScaleTests(unittest.TestCase):
    def setUp(self):
        self.capacity = 5000000
        self.lru_cache = LRUCache(self.capacity)
        
        for i in xrange(1, self.capacity + 2):
            self.lru_cache.set('user' + str(i), 'user_number_' + str(i))

    def tearDown(self):
        self.lru_cache = None

    @raises(KeyError)
    def test_set_and_get(self):
        """
        lru element should be user2 and user1 sould be removed.
        """
        self.assertEqual(self.lru_cache.get_lru_el(), 'user2')
        self.lru_cache.get('user1')

    def test_update(self):
        """
        test update
        """

        self.lru_cache.set('user' + str(self.capacity/2), 'ANON_USER')
        self.assertTrue(self.lru_cache.get('user' + str(self.capacity/2)) == 'ANON_USER')

        self.lru_cache.set('user2', 'USER2')
        self.assertEqual(self.lru_cache.get_lru_el(), 'user3')


