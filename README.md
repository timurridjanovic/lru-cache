#LRU Cache

**Description**:
This project is a bit of an experiment and involves 3 different LRU Cache implementations. One uses a min heap (often used in priority queues) instead of an OrderedDict, the second one uses the built-in OrderedDict from the collections package, and the last one uses my own simple implementation of an OrderedDict.

**Observations**:
All three LRU Caches have the same tests. I ran some tests for scale with a capacity of 5 000 000 elements in the cache and added an additional 500 002 elements. Obviously, the min heap has a Big O(log n) for inserts, updates and deletes, so it is much slower than the OrderedDict, which has a Big O(1). That said, the min heap is actually slightly faster until you reach the cache's capacity.

**Prolifing of 3 different caches with a 5 000 000 element capacity:**

|  Number of inserted Elements  |  Min Heap    |  OrderedDict  |  MyOrderedDict  |
|:-----------------------------:|:------------:|:-------------:|:---------------:|
| 5 000 000                     |  47.626s     |  52.375s      |  59.921s        |
| 5 500 002                     |  147.524s    |  62.620s      |  69.016s        |

**Run tests**:
To run the tests, you need to have nose installed. If you're on a UNIX-like system, you can run `easy_install nose` or `pip install nose` 
(you'll probably need to run these commands as root or using sudo).

Once nose is installed, you can simply run `nosetests` in either of the 3 LRU Cache directories.


