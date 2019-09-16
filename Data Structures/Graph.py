## Implementation of Graph with edge addition
import deque
class Graph:
    def __init__(self,n):
        self.neighbours={}
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
        
