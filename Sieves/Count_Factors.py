def count_factors(n):
    ##Count number of factors of numbers from 1 - N
    count_factor=[1]*(n+1)
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            count_factor[j]+=1
    
    return count_factor

    
    
