print("Output of Q.1")
a= int(input("Enter values of a for quadratic equation ax**2+bx+c="))
b= int(input("Enter values of b for quadratic equation ax**2+bx+c="))
c= int(input("Enter values of c for quadratic equation ax**2+bx+c="))
d=b**2-4*a*c
if d<0:
    print("No real roots")
elif d==0:
    print(-b/2*a)
else :
    print((-b+(d**(1/2)))/2*a,(-b-(d**(1/2)))/2*a)