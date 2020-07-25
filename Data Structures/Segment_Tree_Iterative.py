# Iterative implementation of minimum segment tree
# 1 based Indexing
# Query [L, R] inclusive
# Padding by default = 1e18, pass lower value if you do not require elements of such order

class SegmentTree:
    def __init__(self, data , pad = 1e18):
        self.pad = pad
        n = len(data)
        self.m = 1
        while self.m < n: self.m *= 2
        
        self.val = [pad] * self.m + data + [pad] * (self.m-n)
        for i in range(self.m - 1, 0 , -1):
            self.val[i] = min(self.val[i << 1], self.val[(i << 1) + 1])
            
    def get_min(self,l,r):
        l += self.m
        r += self.m
        min_element = self.pad
    
        while l <= r:
            if l & 1:
                min_element=min(min_element, self.val[l])
                l += 1
            if (r + 1) & 1:
                min_element=min(min_element, self.val[r])
                r -= 1
            l >>= 1
            r >>= 1
    
        return min_element
    
    def update(self, i, element):
        i += self.m 
        self.val[i] = element
        i >>= 1
        while i:
            x = i << 1
            self.val[i] = min(self.val[x] , self.val[x + 1])
            i >>= 1
    
