from random import randint as rand

##Miller rabin, increase iterations to improve accuracy
def miller_rabin(p):
    if p<2 or p%2==0:
        return False
    n=p-1
    r=0
    while n%2==0:
        n=n//2
        r+=1
    
    iterations=rand(10**2,10**3)
    for i in range(iterations):
        a=rand(2,p-2)
        x=pow(a,n,p)
        if x==1 or x==p-1:
            continue
        
        for i in range(r-1):
            x=(x*x)%p
            if x==1:
                return False
            if x==p-1:
                flag=1
                break
        if flag==1:
            continue
        return False
    return True
