numb = 5
print(type(numb))

floatnumb = 5.226
print(type(floatnumb))

newfloatnumb = float(numb)
print(newfloatnumb)

name = '1254'
newint = int(name)
newint
1254
a = 0.1
b = 0.001
print(b < a)

Marks = [89, 88, 78, 98, 97]
print(type(Marks))

Marks.append(56)


print(Marks.index(89))

print(Marks.sort())


grades = (1, 3, 4, 5)
print(type(grades))

print(grades.count(3))

print(grades.index(4))

percentage = {89.5, 69.5, 78.7, 87}
print(percentage.add(91))

print(percentage)
{69.5, 78.7, 87, 89.5, 91}

#Sets
#do not support the indexing
#No dublication
#Unordered
TeamA = {12, 45, 14, 85, 45}
TeamB = {12, 45, 89, 74, 52}
TeamUnion = TeamA.union(TeamB)# print unique elemtents from both the sets
print(TeamUnion)

TeamA.symmetric_difference(TeamB)
print(TeamA)
TeamA.issuperset(TeamB)
print(TeamA)

TeamA.isdisjoint(TeamB)
print(TeamA)
TeamA.update(TeamB)
print(TeamA)


#Dictionary
Name = {'Balaji', 'Arun', 'Ajit'}
# Marks={''88','89','91''}
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
##Marks={''88','89','91'}
...
# SyntaxError: unterminated string literal (detected at line 1)
Marks = {'88', '89', '91'}

ClassA = dict(zip(Name, Marks))
print(ClassA)

ClassA.update({'karun': '82'})

print(ClassA)

print({78.7, 69.5}.issubset(percentage))



print('Balaji' in ClassA)




