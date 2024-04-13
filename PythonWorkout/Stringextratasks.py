user = '''Heloo-'"" user '''# mulit string initialization
user1=('Hello')
res=user+user1
print(res)
#Length of a string
print(len(user))
#size(my_string)
#print(user.length())


if "Balaji" in "Balaji154":
    print("Balaji")
else:
    print("Nothing")
#Pyhton conditional statement has contain method to compare ,
#Python has not got the "has " Keyword
#The ~ symbol is not used for string comparison in Python.

string = "Balaji learning python"
substring = "python"
index = string.find(substring)
if index!=-1:
    print("Substring {} is found in {} index ".format(substring,index))
else:
    print("Not found")
#takaway is to find substring in python is find() and index method



string = "Balaji learning python"
substring = "Balaji learning java"
if substring.startswith("Balaji"):  #substring, index number erepplace this "Balaji"
    print("It start with balaji")

else:
    print("None")


#Join method will acts like concat or additon which is one iterable such as tuble, list, dict

my_list = ["apple", "banana", "orange"]
result = ", ".join(my_list)
print(my_list)
print(result)

#How to sepaete the string in comma delimiter
my_string = "apple,banana,orange"
result = my_string.split(",")
print("Coomma",result)


#how do we print the number using format

number = 42
formatnumb = f" the number is {number}"
print(formatnumb)
number = 123
print("The number is {}".format(number))