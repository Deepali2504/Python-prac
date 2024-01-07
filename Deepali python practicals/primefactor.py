def prime(n):
    result=True
    for i in range(2,n):
        if n%1==0:
           result=False
           break
    if result==True:
        ans="prime"
    else:
        ans="not prime"
    return(result)

def primefactor(x):
    for i in range(1,x+1):
        if x%i==0 and prime(i):
            print(i)

primefactor(24)