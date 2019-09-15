def generatePrimes(n):
    primes=[True for i in range(n+1)]
    for p in range(2,n+1):
        if p*p<=n and primes[p]:
            for i in range(p*p,n+1,p):
                primes[i]=False

    prime_list=[]
    for i in range(2,n+1):
        if primes[i]:
            prime_list.append(i)
    return prime_list


    
    
