## Djikstras Implemented using priority queue , Time complexity ~ ElogV , 0 based indexing for vertices

import sys
import heapq
INT_MAX=sys.maxsize
class WeightedGraph:
    def __init__(self,n):
        self.neighbours={}
        self.n=n
        for i in range(0,n):
            self.neighbours[i]=[]
    
    def addEdge(self,u,v,weight):
        self.neighbours[u].append((v,weight))
        self.neighbours[v].append((u,weight))
    
    def djikstra(self,source):
        dist=[INT_MAX]*self.n
        dist[source]=0
        unvisited=[(0,source)]
        heapq.heapify(unvisited)
        seen=set()
        for i in range(n):
            d,u=heapq.heappop(unvisited)
            if u in seen:
                continue
            seen.add(u)
            for v in self.neighbours[u]:
                if v[0] in seen:
                    continue
                dist[v[0]]=min(dist[v[0]],dist[u]+v[1])
                heapq.heappush(unvisited,(dist[v[0]],v[0]))
        return dist
