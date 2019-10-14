from random import randint as rand

##Fermat's little theorem for probabilistic primality testing, p=number to check, more the iterations more the accuracy
def fermat(p,iterations):
    if p==1:
        return False
    for i in range(iterations):
        a=rand(1,p-1)
        if pow(a,p-1,p)!=1:
            return False
    return True

