class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.exist = 0
        self.parent = None

class BitTrie:
    def __init__(self, data):
        self.root = Node()
        for val in data:
            current = self.root
            
            for i in range(29, -1, -1):
                prev = current
                if (val >> i) & 1 == 0:
                    if current.left == None:
                        current.left = Node()
                        
                    current = current.left
                else:
                    if current.right == None:
                        current.right = Node()
                    current = current.right
                current.parent = prev
                    
            current.exist += 1
        
    def find_min(self, val):
        cost = 0
        current = self.root
        for i in range(29, -1, -1):
            if (val >> i) & 1 == 0:
                if current.left != None:
                    current = current.left
                else:
                    cost += 1 << i
                    current = current.right
            else:
                if current.right != None:
                    current = current.right
                else:
                    current = current.left
                    cost += 1 << i
                    
        return cost
    
    def remove(self, val):
    
        current = self.root
        for i in range(29, -1, -1):
            if (val >> i) & 1 == 0:
                current = current.left
            else:
                current = current.right
        
        current.exist -= 1
        
        if current.exist == 0:
            
            
            while 1:
                parent = current.parent
                if parent == None:
                   
                    break
                if parent.left != None and parent.right!=None:
                    
                    if parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                    break
                else:
                    
                    parent.left = None
                    parent.right = None
                
                current = parent
    
    def add(self, val):
        current = self.root
        for i in range(29, -1, -1):
            if (val >> i) & 1:
                if current.right == None:
                    current.right = Node()
                current = current.right
            else:
                if current.left == None:
                    current.left = Node()
                current = current.left
        current.exist += 1
