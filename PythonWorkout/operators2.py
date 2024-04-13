
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
def loop_value():
    user_value = int(input("Enter a value (1-100): "))
    if 1 <= user_value <= 100:
        for i in range(1, user_value):  # this line of code i have just entered the user_value not + 1 , or 2 or any other
            print(i)
    else:
        print("Please enter a value between 1 and 100.")

loop_value()



def loop_value2():
    user_value2 = int(input("Enter a number :"))
    for i in range(1,user_value2):
        print(i)


loop_value2()


