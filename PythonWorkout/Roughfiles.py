
float1= 125
print(float)
my_float = float(float1)
print(my_float)

a=5
b=6

print(c)
c=a.be


myfloat = 7.0
print(myfloat)
myfloat = float(129)
print(myfloat)


mylist =[]
mylist.append(10)
mylist.append(15)
mylist.append(20)
mylist.append(14)
mylist.append(80)
print(mylist)
for i in mylist:
    print(i)




mylist=[10, 15, 20, 14, 80]
mylist1=[10, 15, 20, 14, 80,25]
c=mylist1+mylist
print(c)

print("desired index are :",mylist[2])
#print(mylist.index(14))
print(f" value are {mylist.index(14)}")


mylist=[10, 15, 20, 14, 80]
try:
    print(mylist.reverse() * 5)
except TypeError as e :
    print("Execute the correct value")
    print(mylist.__len__())
    res=mylist[::2]
    print(res)






name = "John"
age=78
print(f"{name} is {age} years old")
print(len(name))
print(name[::1])

