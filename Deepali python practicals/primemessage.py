def primemessage(n):
    result=True
    for i in range(2,n):
        if n%i==0:
            result=False
            break
    if result==True:
        print("The given number",n,"is a prime number")
        print("This done by primemessage function")
    else:
        print("This done by primemessagefunction")

primemessage(4)
primemessage(5)


