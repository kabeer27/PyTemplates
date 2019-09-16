## Code to calculate nCr under modulo p (mod)
mod=10**9+7
factorial=[1]

def preCalculate(n):
    for i in range(1,n+1):
        factorial.append(factorial[-1]*i%mod)

def nCr(n,r):
    return ( ( factorial[n]*pow(factorial[r],mod-2,mod)*pow(factorial[n-r],mod-2,mod) )%mod )

n=int(input())
preCalculate(n)
