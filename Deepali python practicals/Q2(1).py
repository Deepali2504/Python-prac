print("The prime number from 1 to 100")
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

def main():
    for i in range(1,101):
        if prime(i)==True:
            print(i, end=" ")


main()