class SegmentTree:
    ##Iterative implementation of minimum segment tree
    def __init__(self,data,pad):
        self.pad=pad
        n=len(data)
        self.m=1
        while self.m<n: self.m*=2
        
        self.val=[0]+[pad]*self.m+data+[pad]*(self.m-n)
        
        for i in range(self.m+n,0,-1):
            self.val[i>>1]=min(self.val[i>>1],self.val[i])
    
    def GetMin(self,l,r):
        l+=self.m
        r+=self.m
        min_element=self.pad
        while l<=r:
            if l&1:
                min_element=min(min_element, self.val[l])
                l+=1
            if (r+1)&1:
                min_element=min(min_element, self.val[r])
                r-=1
            l>>=1
            r>>=1
        return min_element
        
    def update(self, i, element):
        i += self.m
        self.val[i]=element
        i>>=1
        while i:
            x=i<<1
            self.val[i]=min(self.val[x],self.val[x+1])
            i>>=1
