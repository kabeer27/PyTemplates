## Program to count number of smaller elements for each element on right hand side, works in O (N log N) Constraint on array value does not matter.

def update(fenwick, idx, val, n):
    while idx<n:
        fenwick[idx]+=val
        idx+=(idx & (-idx))

def get_sum(fenwick, idx):
    sum=0
    while idx>0:
        sum+=fenwick[idx]
        idx-=(idx & (-idx))
    return sum

def count_smaller_elements(arr):
    temp=arr.copy()
    temp.sort()
    curr_size=1
    Hashed_Value={}
    ## Hashing values so that we can implement fenwick of size N instead of size Max Value
    for item in temp:
        if item not in Hashed_Value:
            Hashed_Value[item]=curr_size
            curr_size+=1
    
    fenwick=[0]*(curr_size)
    
    for i in range(n):
        temp[i]=Hashed_Value[arr[i]]
    temp=temp[::-1]
    count_smaller=[0]*n
    
    for i in range(n):
        count_smaller[i]=getSum(fenwick, temp[i]-1)
        update(fenwick, temp[i] , 1 ,curr_size)
    return count_smaller[::-1]
    
n=int(input())
arr=list(map(int,input().split()))
print(count_smaller_elements(arr))
