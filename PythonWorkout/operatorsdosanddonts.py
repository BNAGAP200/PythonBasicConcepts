a='Ragu'
b='Vinay'
c=a+b


#c = a.join(b) #only for iteratrion such as list, tuble,
#c = a.concat(b)
#c = a .. b

#How do you get a part of a string?
part =b[2:3]
#part = string / 2 / 3
#part = string.substring(2, 3)
#part = string[2::3]

d= [3,4,5,6,7,8,9]
e=d[::2] #Print all even location numbers
print(e)
f=d[0::]
print(f)


#How do you use the integer division operator?
c=5
d=10

int_div = c// d
#int_div = a.intdiv(b)
#int_div = a div b
#int_div = a : b


#How do you use the modulus operator?

int_div = c % d
print(int_div)
#int_div = a.mod(b)
#int_div = a mod b
#int_div = a :: b

x=3
y=8
#How do you check if a variable is between two numbers?

if x < 3 or x > 5:
    print("x is between 3 and 5")
if x < 3 and x > 5:
    print("x is between 3 and 5")

if 3 < x < 5:
    print("x is between 3 and 5")
#How do you check if two variables are true?

#if (a, b) is True:#compare for the tuble
    print("a and b are true")
if a and b:
    print("a and b are true")
#if a = True and b = True: #For comparison two equal sign should be there
    print("a and b are true")
#if a && b: #pyhton there is no existence of &&
    print("a and b are true")


#How do you execute a bitwise AND operation between two numbers?
c= a & b
#c = a && b: This syntax is incorrect in Python. The && operator is used for logical AND operations in languages like C, C++, and Java, not for bitwise AND operations. In Python, && is not valid for bitwise operations.

# = a & b: This is the correct syntax for performing a bitwise AND operation between two numbers in Python. It performs a bitwise AND operation between the binary representations of a and b.

#c = a and b: This is not a bitwise operation. It's a logical AND operation which evaluates to True if both a and b are true, otherwise False.

#c = a | b: This performs a bitwise OR operation, not a bitwise AND operation.


