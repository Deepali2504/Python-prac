# l1=eval(input("Enter the list: "))
# l2=[]
# for i in l1:
#     if type(i)==int:
#         if i%2==0:
#             j=i**3
#             l2.append(j)


# print("The list of cubes of cubes of the even integers that are entered in the list is as follows:", l2)


# l3=[x**3 for x in l1 if type(i)==int and x%2==0]
# print("The list of cubes of cubes of the even integers that are entered in the list is as follows:", l3)


#def dictionary_1_to_5():
 #   d1=dict()
 #   for i in range(1,6):
 #       d1[i]=i**3
 #   print(d1)

#dictionary_1_to_5()

    
t1=(1,2,5,7,9,2,4,6,8,10)
# length=int(len(t1))
# half_length=int(length/2)

# print(t1[1:half_length+1])
# print(t1[half_length:length])


t3=tuple([x for x in t1 if x%2==0])
print("The tuple with only the even integer present in t1 as follows:",t3)


t2=(11,13,15)
print("The concatenated tuple is as follows:",t1+t2)


print("The maximum value present in t1 is:" , max(t1))
print("The minimum value present in t1 is: ", min(t1))
