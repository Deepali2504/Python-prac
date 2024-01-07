# Ques.1
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# d=int(input("Enter fourth  number:"))
# e=int(input("Enter fifth number:"))
# x=(a+b+c+d+e)
# y=(x/5)

# print("Sum of numbers:", x)
# print("Average of Numbers:",y)




#Ques.4
# print("sum of squares of the 5 numbers is,",((a**2)+(b**2)+(c**3)+(d**4)+(e**2)))





#Ques.2
# print("Area of rectangle")
# length=int(input("Enter length:"))
# width=int(input("Enter width:"))
# area=length*width
# print("Area", area, "sq. units")




#Ques.3
# print("To find datatype of data")
# f=eval(input("enter first data:"))
# g=eval(input("enter second data:"))
# h=eval(input("enter third data:"))
# i=eval(input("enter fourth data:"))
# print("Datatype of first data is,",type(f))
# print("Datatype of first data is,",type(g))
# print("Datatype of first data is,",type(h))
# print("Datatype of first data is,",type(i))




#Ques5
# print("Table")
# print("A\tb\t A**B")
# print("1\t2\t    1")
# print("2\t3\t    8")
# print("3\t4\t   81")
# print("4\t5\t 1024")
# print("5\t6\t15625")




#Ques.6
print("To calcualte area of triangle")
x1=int(input("enter point x1:"))
y1=int(input("enter point y1:"))
x2=int(input("enter point x2:"))
y2=int(input("enter point y2:"))
x3=int(input("enter point x3:"))
y3=int(input("enter point y3:"))
print("The coordinates are",(x1,y1),(x2,y2),(x3,y3))
print("then the length of the sides will be as follows:")
AB=(((x2-x1)**2)+((y3-y2)**2))**0.5
print("AB",AB,"units")
BC=(((x3-x2)**2)+((y3-y2)**2))**0.5
print("BC",BC,"units")
CA=(((x1-x3)**2)+((y1-y3)**2))**0.5
print("CA",CA,"units")
S=((AB+BC+CA)/2)
Area=(S*(S-AB)*(S-BC)*(S-CA))**0.5
print("AREA OF TRIANGLE IS",Area,"sq.units")










