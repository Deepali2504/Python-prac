def nf():
    x=int(input("enter a no: "))
    d=1
    for i in range(1,x+1):
            d=d*i
            i+=1
    return d 
    
print(nf())