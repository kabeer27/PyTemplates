class DSU:
    def __init__ (self,n):
        self.parent=list(range(n))
        self.size=[1]*n
        self.count_sets=n
    
    def find(self,u):
        to_update=[]
        while u!=self.parent[u]:
            to_update.append(u)
            u=self.parent[u]
        for v in to_update:
            self.parent[v]=u
        return u
    
    def union(self,u,v):
        u=self.find(u)
        v=self.find(v)
        if u==v:
            return
        if self.size[u] < self.size[v]:
            u,v=v,u
        self.count_sets-=1
        self.parent[v]=u
        self.size[u]+=self.size[v]
    
    def set_size(self,a):
        return self.size[self.find(a)]
    
    def set_count(self):
        return self.count_sets
