# To check number is prime or not.
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return 'True'
    else:
        return 'False'
# To generate prime no. till n
def primeno(n):
    for i in range(1,n):
        if prime(i)=='True':
            primeno1.append(i)
        else:
            pass
    print(primeno1)
# To generate first n prime no.
def fprime(n):
    x=2
    while True:
        if prime(x)=="True":
            prime_number.append(x)
        if len(prime_number)==n:
            break
        else:
            x+=1
    for i in prime_number:
        print(i)
# main function.
def main():
    n=int(input("Enter a number:"))
    print(prime(n))
    print("Prime number till n are:-")
    print(primeno(n))
    print("First n prime numbers are:-")
    print(fprime(n))
prime_number=[]
primeno1=[]
main()
