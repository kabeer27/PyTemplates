from collections import deque
class LCA:
    def __init__(self, n, edges):
        # Assuming Tree is rooted at 1
        q = deque()
        q.append(1)
        self.parents = [ [1]*18 for _ in range(n+1)] 

        self.depth = [-1] * (n + 1)
        self.depth[1] = 0
        
        while q:
            u = q.popleft()
            for v in edges[u]:
                if self.depth[v] == -1:
                    q.append(v)
                    self.depth[v] = self.depth[u] + 1
                    self.parents[v][0] = u
                    
                    for i in range(1,18):
                        self.parents[v][i] = self.parents[self.parents[v][i-1]][i-1]
    
    def get_parent(self, node, dist):
        while dist:
            i = dist.bit_length() - 1
            node = self.parents[node][i]
            dist ^= 1 << i
        return node
    
    def get_lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        v = self.get_parent(v, self.depth[v] - self.depth[u])
        
        for i in reversed(range(18)):
            pu = self.parents[u][i]
            pv = self.parents[v][i]
            
            if pu!=pv:
                u = pu
                v = pv
        return u if u == v else self.parents[u][0]

