##Follows 1 based indexing for nodes, supports directed and undirected graphs, topological sort for directed graphs added

from collections import deque
class Graph:
    def __init__(self,n):
        self.neighbours={}
        self.n=n
        for i in range(1,n+1):
            self.neighbours[i]=[]
    
    def addDirectedEdge(self,u,v):
        self.neighbours[u].append(v)
    
    def addEdge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)

    def neighbhours(self,u):
        return self.neighbours[u]

    def bfs(self,source):
        queue=deque()
        queue.append(source)
        visited=[0]*n
        visited[source-1]=1
        while queue:
            u=queue.popleft()
            for v in self.neighbours[u]:
                if visited[v-1]==0:
                    visited[v-1]=1
                    queue.append(v)
        return visited
    
    def dfs(self,source):
        stack=[source]
        visited=[0]*n
        visited[source-1]=1
        while stack:
            u=stack.pop()
            for v in self.neighbours[u]:
                if visited[v-1]==0:
                    visited[v-1]=1
                    stack.append(v)
        return visited
    
    def topologicalSort(self):
        Order=[]
        visited=[0]*self.n
        in_degree=[0]*self.n
        for u in range(1,n+1):
            for v in self.neighbours[u]:
                in_degree[v-1]+=1
        q=deque()
        for u in range(n):
            if in_degree[u]==0:
                q.append(u+1)
                visited[u]=1
        while q:
            u=q.popleft()
            Order.append(u)
            for v in self.neighbours[u]:
                in_degree[v-1]-=1
                if in_degree[v-1]==0:
                    q.append(v)
                    visited[v-1]=1
        return Order
