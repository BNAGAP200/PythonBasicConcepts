'''def nos(x, y):
    x=5
    y=8
    return x, y
x,y = nos(0,0)
print(x+y)
print(x-y)


def letts(a,b):
    a='first alphabet'
    b='second alphabet'
    return a,b
a,b = letts(0,0)
print(letts(a,b)) '''


# Arbitrary keyword
def person(age, **data):
    print(age)
    print(data)


person(28, city='Mumbai', mob=542542)


# default parameter
def nations(coutry='India'):
    print(coutry)


nations('africa')
nations('england')


# List as an  argument

def food(spices):
    for x in spices:
        print(x)


spices = ["clove", "cardomon", "barklev"]
food(spices)


# return values
def math(x):
    return 5 + x


print(math(3))
print(math(9))
