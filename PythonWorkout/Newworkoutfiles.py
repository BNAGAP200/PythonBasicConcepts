try:
    user_input = int(input("Enter a number: "))
    user_input1 = int(input("Enter another number: "))
    c = user_input / user_input1
    print( c)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

#index error

try:
    A= [1,2,5,7,8,]
    b={1,5,4,8,7}
    print(A[10])

except IndexError:
    print("out of zeroindex")



#Key error#
try:
    Marks = {'Maths' : 85,'Science' :92,'English' :88 }
    print(Marks['Art'])

except KeyError:
    print("Showing key error")


