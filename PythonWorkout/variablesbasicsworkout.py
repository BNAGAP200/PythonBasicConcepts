
#How to initialize the list of variables
my_array = list([1, 2, 3])
print(my_array)
my_list= [1,3,4,5,6,7,8]
print(my_list)
#my_array = list(1, 2, 3)
#my_array = {1, 2, 3}

my_dict ={}
print(my_dict)
#my_dict = new Dictionary()
#my_dict = dict[]
#my_dict := {}

my_set =()
my_set1 =set()
print(my_set1)
print(my_set)
#myset1= set[]
#my_set = new Set()
#my_set := {}

my_string1 ='Hello all!'
my_string2=str("hello!")
print(my_string1)
print(my_string2)
#my_string1 = string(Hello!)
#my_string := "Hello!"

my_int =55
print(my_int)


my_float=55.5
print(my_float)

#my_float1 = 5.0f are wrong shows syntax error
#my_float=7f
#my_float := float(7)


#how do check the type of variable
print(type(my_int))
#var.type()
#typeof(var)

del my_int
#print(my_int)
#var := 0
#var = None
#delete(var)

#how do we representation
my_list = [42, 'hello', [1, 2, 3], {'a': 1, 'b': 2}, (4, 5, 6)]

for item in my_list:
    print(repr(item))


#how to initalize a bytes
my_bytes = bytes()
#my_bytes = new Bytes()
#my_bytes := b""
#my_bytes = bytes[]


#how to initalize a tuble with two numbers
my_tuple = (1, 2)
#my_tuple = [1, 2]
#my_tuple = Tuple([1, 2])
#my_tuple = tuple(1, 2)

#How to assign a two variables from tuble
a, b = (1, 2)
#a : b = (1, 2)
#assign((a, b), (1, 2))