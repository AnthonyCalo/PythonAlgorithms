
'''
Really interesting solution.
 One of the first times i've actually used a linked list to solve a problem

Really elegant
'''

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.collections=dict()
        self.head=ListNode(0,0)
        self.tail=ListNode(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head

        
    def get(self, key: int) -> int:
        if(key in self.collections):
            node=self.collections[key]
            self.rem_from_list(node)
            self.insert_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.collections:             # similar to get()        
            node = self.collections[key]
            self.rem_from_list(node)
            self.insert_head(node)
            node.val = value         # replace the value len(dic)
        else: 
            if len(self.collections) >= self.capacity:
                self.rm_from_tail()
            node = ListNode(key,value)   
            self.collections[key] = node #this creates a dictionary with key equal to 
            self.insert_head(node) # the number being appended and value=a listNode objec
        
    def rem_from_list(self, node):
        last=node.prev
        nextNode=node.next
        last.next=nextNode
        nextNode.prev=last
        
    def insert_head(self, node):
        headNext=self.head.next
        self.head.next=node
        node.next=headNext
        node.prev=self.head
        headNext.prev=node
    def rm_from_tail(self):
        if(len(self.collections)==0): return
        tail_node = self.tail.prev
        del self.collections[tail_node.key]
        self.rem_from_list(tail_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4'''