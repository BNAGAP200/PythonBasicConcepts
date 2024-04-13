
age=5
c=age*2
print(c)

age =5
age*2
print(age)

def opt_value():
    name='Balaji'
    age=28
    try:
     res=name+age
     print(res)
    except TypeError:
     print("You should convert int into string first")

    a=5
    b=6
    c=a*b
    print(c)

opt1=opt_value()

def loop_value():
    user_value = int(input("Enter a value "))

    for i in range(user_value):
        print(i)

    user_value2 = bool(input("Enter a value"))

    for i in range(user_value2):
        print(i)



l=loop_value()
