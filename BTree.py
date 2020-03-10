class BNode:
    
    '''
    Attributes
    Docstring: Class to create a node of a BTree
    leaf: Represents the leaf of the tree
    keys: Represents a list of present keys in each node
    children: Represents a list of children nodes
    
    '''
    
    def __init__(self, leaf=False):
        
        '''
        Docstring: Method for initialization
        Parameters: leaf, default value is False
        
        '''
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    
    '''
    Dosstring: Class containing all the methods to create a B Tree, split child, insert node and search for a node
    
    '''
    
    def __init__(self, t):
        
        '''
        Docstring: Method for intitalization
        Parameter: t, integer value representing minimum keys (t-1) in each node
        
        '''
        
        self.root = BNode(leaf = True)     
        self.t = t
        
        
        
    def search(self, k, x=None):
        
        '''
        Docstring: Method for searching an element
        Parameters: k, x
        Input: k: a key value to be searched; x: a root node from where the search is to be initiated (optional)
        Output: Returns whether the element is present or absent
        
        '''

        if isinstance(x, BNode):                                  #isinstance() checks if x is the node of Btree
            i = 0
            while i < len(x.keys) and k > x.keys[i]:              #Searching for the appropriate node to start search
                i += 1
            if i < len(x.keys) and k == x.keys[i]:                #if the value is present
                print('Key Present')
                return
            elif x.leaf:                                          #if the search ends and element is not found
                print('Key not Present')
                return
            else:
                return self.search(k, x.children[i])              #recursive call with the children of x
        else:
            return self.search(k, self.root)                      #if x=None, the recursive call with root
    
    def insert(self, k):
        
        '''
        Docstring: Method to insert an element into the node
        Parameter: k
        Input: A key value to be inserted
        Output: Root after inserting the key
        
        '''
        r = self.root
        if len(r.keys) == (2*self.t) - 1:                         #checks if the keys in the node has reached it max capacity
            s = BNode()                                           #creating a new node of BNode
            self.root = s
            s.children.append(r)                                  #None root is appended as the child node
            self.split_child(s, 0, r)                             #split_child method call
            self.insert_nonfull(s, k)                             #insert key value in a non full node
        else:
            self.insert_nonfull(r, k)                             #insert key value in a non full node
            
    def split_child(self, x, i, y):
        
        '''
        Docstring: Method to split a node into a root and a child node
        Parameter: x, i, y
        Input: x: parent node; i: index value; y: parent node
        Output: A split node having parent & child node
        
        '''
        t = self.t
        z = BNode(leaf = y.leaf)                                 #creating a new node z, having same leaf value as of y
        
        x.children.insert(i+1, z)                                #insert the children of x into z at index value i + 1
        x.keys.insert(i, y.keys[t-1])                            #insert keys of y at t-1, into keys of x at position i
        z.keys = y.keys[t:]                                      #split y node, assigning to z, from t to end element
        y.keys = y.keys[0:t]                                     #y is reassigned with keys from 0 to t
                
        if not y.leaf:                                           #checks whether the y node is a leaf node or not
            z.children = y.children[t:]                          #if y is not leaf, assign y children from t to end, to z children
        
        for j in range(len(x.keys), i, -1):
            x.children.insert(j+1, x.children[j])                #shift all the elements of children of x to one next position
        x.children.insert(i+1, z)                                #insert z elements at the first position in children node of x
        
        for j in range(len(x.keys)-1, i-1, -1):
            x.keys.insert(j+1, x.keys[j])                        #shift all the elements of x keys to the next position
        x.keys.insert(i, y.keys[t-1])                            #insert element of y.key at t-1 at i in x.keys
            
    def insert_nonfull(self, x, k):
        
        '''
        Docstring: Method to insert element in a non full node
        Parameter: x, k
        Input: Node x & key value k, to be inserted
        Output: Inserts a key and returns with the root node
        
        '''
        t = self.t
        i = len(x.keys) - 1                                      #assign i value with the n[x] - 1
        if x.leaf:                                               #checks whether x is a leaf node or not
            x.keys.append(0)                                     #if x is a leaf node, append an element (0) in list x.keys
            while i >= 0 and k < x.keys[i]:                     
                x.keys[i+1] = x.keys[i]                          #shifts elements of x.keys to next position until i >= 0 & k < key[x]
                i -= 1                                           #i decrementer
            x.keys[i+1] = k                                      #enter the new element in the decided position
        else:
            while i >= 0 and k < x.keys[i]:                      #if x is not a leaf node
                i -= 1                                           #decrement i until i >= 0 & k < key[x]
            i += 1                                               #increment i by 1
            if len(x.children[i].keys) == 2 * t - 1:             #checks whether node is full 
                self.split_child(x, i, x.children[i])            #if node is full, call split_child method with x node, index & child of x
                if k > x.keys[i]:                                #checks whether k > key[x]
                    i += 1                                       #increment i by 1
            self.insert_nonfull(x.children[i], k)                #recursive call with child of x and the key to be inserted
    

ob = BTree(3)
for i in range(0, 15):
    ob.insert(i)

for i in range(0, 15):
    ob.search(i)