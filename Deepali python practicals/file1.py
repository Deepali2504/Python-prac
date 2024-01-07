def prime(x):
    result=True
    for i in range(2,x):
        if x%i==0:
            result=False
            break 
    if result==True:
        ans="prime"
    else:
        ans="not prime"
    return(result)