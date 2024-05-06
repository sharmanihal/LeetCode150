class Node:
    def __init__(self,key,val=0):
        self.key=key
        self.val=val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        # This dictionary will map keys to corresponding nodes in the doubly linked list.
        self.cache={}
        # Initialize the doubly linked list with two sentinel nodes, left and right.
        # These sentinel nodes will help in managing the least recently used and most recently used nodes.
        self.left,self.right=Node(0),Node(0)
        self.left.next=self.right
        self.right.prev=self.left
        
    # Helper function to remove a node from the doubly linked list.
    def remove(self,node):
        prevNode,nextNode=node.prev,node.next
        prevNode.next=nextNode
        nextNode.prev=prevNode
        
    # Helper function to insert a node at the right most postion into the doubly linked list.
    def insert(self,node):
        prevNode,nextNode=self.right.prev,self.right
        prevNode.next=nextNode.prev=node
        node.next=nextNode
        node.prev=prevNode

    def get(self, key: int) -> int:
        if key in self.cache:
            # If the key exists in the cache, remove the corresponding node from its current position
            # and insert it at the beginning(right most) to mark it as the most recently used.
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key already exists in the cache, remove its corresponding node.
            self.remove(self.cache[key])
        # Create a new node with the given key and value.
        self.cache[key]=Node(key,value)
        # Insert the new node at the beginning(right most) to mark it as the most recently used.
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            # If the cache size exceeds the capacity, remove the least recently used node,
            # which is pointed by the left pointer.
            lru= self.left.next
            self.remove(lru)
            # Delete the least recently used key from the cache dictionary.
            del self.cache[lru.key]
            
"""
Explanation:
- The code implements an LRUCache class with a doubly linked list and a dictionary to achieve O(1) time complexity for both get and put operations.
- Each node of the doubly linked list represents a key-value pair.
- The dictionary `cache` stores key-node mappings for quick access to nodes.
- The doubly linked list maintains the order of access, with the most recently used node at the end and the least recently used node at the beginning.
- The `get` method retrieves the value associated with a given key, updates the order of access, and returns the value.
- The `put` method inserts or updates a key-value pair in the cache, evicts the LRU node if the cache is full, and updates the order of access.
- Helper functions `remove` and `insert` are used to manipulate the doubly linked list efficiently.
- Overall, the implementation ensures O(1) average time complexity for both get and put operations by using a combination of dictionary and doubly linked list.
"""
