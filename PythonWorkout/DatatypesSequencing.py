# for naming conventions >>snake-case presfarrabel


# Numeric date types>>int, float, complex number

# int>>(contains -ve and +be numbers , there will no limit for declaring integer
# Float>.decimal point,(positive nad negative numbers
# complex> real part and imaginary part

# what cannot  to do
# tubles and strings are modified or immmutable
# arithmatic operations can not perform at strings
# accessing non-existent dictionary keys
# index out of range cannot perform at any operations

# list of errors
# Typeerror(adding or perfroming in-appropriate data type(5+'hello')
# valueerror>>int('hello') receives the argument of righttyp with an inapproriate value
# indexerror >>>out of range
# keyerror  >>> when a dictionary key is found
# zerodivisionerror >>>
# attributeerror
# overflowerror>>> arithmetic is tool large to be represented

a = [5, 8, 7, 5, 4]

b = [8, 5, 77, 89, 8]

c = [8, 9, 5, 7, 4, 8]
print(a < c < b)  # false because of python evaluated element wise first,eg 8==8 then jumbs into next 5 and 9

print(a <= b != c * 2)  # true ,Because first pair prove as True so rest will accept as true
print(a.append(7))
print(a)
print(a.index(4))
print(a.count(8))
result = [x + y + z for x, y, z in zip(a, b, c)]
print(
    result)  # here  a and b values are separated to xand y and merge two or add two values using zip() in tuble format
# zip(a, b,c) this part iterates ove the tubels produced zip(a,b) upacking each tuble into variable x, y,z

# ///////////////////#

# i want one element form A will add every element from B
element_to_add = a[0]
for i in range(len(b)):
    b[i] += a[0]

print(b)

# concetenating both the tubles

a = (1, 23, 4, 8, 9, 10)
b = (3, 5, 4, 7, 9, 25)
c = (8, 7, 9, 6, 5, 4)
result = tuple(x + y - z for x, y, z in zip(a, b, c))
print(c)

#Since tubles are immutable and original tubles are unchanged


