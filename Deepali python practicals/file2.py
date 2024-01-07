from file1 import prime
n1=int(input("Enter a number n1:"))
n2=int(input("Enter a number n2:"))
for i in range(n1,n2+1):
    if prime(i)==True:
        print(i, end=" ")