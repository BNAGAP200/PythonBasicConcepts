from array import *

vales = array('I', [5, 9, 4, 2, 3])
print(vales)
print(sorted(vales))

vales1 = array("i", [5, 9, 63, 5, -8])

print(vales1.reverse())
print((vales1))
for vales1 in range(63):
    print(vales1)

vales2 = array('u', ['a', 'c', 'd'])
print(vales2)


#user input

arr= array('i',[])

n = int(input("Enter the length of an array: ?"))
for i in range(4):
     x=int(input("Enter a next value: ?"))
     arr.append(x)

     print(arr)
     print(arr.index(2))