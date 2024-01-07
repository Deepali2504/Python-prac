def fact(x):
    d=1
    for i in range(1,x+1):
        d=d*i
        
    return(d)

def main(n,r):
    nCr=fact(n)/(fact(r)*fact(n-r))
    print("nCr of",n,"and",r,"is :", nCr)

main(50,6)