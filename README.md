#LRU Cache

**Description**:
This project is a bit of an experiment and involves 3 different LRU Cache implementations. One uses a min heap (often used in priority queues) instead of an OrderedDict, the second one uses the built-in OrderedDict from the collections package, and the last one uses my own simple implementation of an OrderedDict.

**Observations**:
All three LRU Caches have the same tests. I ran some tests for scale with a capacity of 500 000 and another with a capacity of 5 000 000 elements in the cache. Even though the min heap has a Big O(log n) for inserts, updates and deletes, it is still slightly faster than both OrderedDict implementations, which should technically be Big O(1). My hypothesis is that this is so because the dictionary needs to rehash everything every time an insert goes over the bucket limit in the hash table. 

|  Capacity  |  Min Heap |  OrderedDict  |  MyOrderedDict  |
|:----------:|:---------:|:-------------:|:---------------:|
|  500 000   |  4.675s   |  4.976s       |  5.756s         |
| 5 000 000  |  47.626s  |  52.375s      |  59.921s        |

**Run tests**:
To run the tests, you need to have nose installed. If you're on a UNIX-like system, you can run `easy_install nose` or `pip install nose` 
(you'll probably need to run these commands as root or using sudo).

Once nose is installed, you can simply run `nosetests` in either of the 3 LRU Cache directories.


