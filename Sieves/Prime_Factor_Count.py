def generatePrimes(n):
    ##Count number of prime factors of numbers from 2 - N , 1 is not counted as a prime number.
    prime_factor_count=[0]*(n+1)
    for i in range(2,n+1):
        if prime_factor_count[i]==0:
            p=i
            while p<n+1:
                prime_factor_count[p]+=1
                p+=i
    return prime_factor_count


    
    
