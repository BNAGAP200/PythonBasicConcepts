
#MathematicalOperators
a=5
b=4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print((a+b),(a-b),(a*b),(a/b))
print((a+b)+(a-b)-(a*b)*(a/b))
print((a/b) ,(a//b))
print(a**b)
print(a/(a**b)-1)

#Assignment Operators

a=7.5
b=8
a +=1

print(a)

a-=1
print(a)

a*=1
print(a)

a += (1 + a) - (1 - a) * (1 * a) // 1
print(a)

#a += 1 + a -= 1 - a *= 1 * a //= 1
# compound assignment operators are cannot chained linked together

x=3
y=5
x^=4
print(x)

x = 3
x ^= 4
print(x)

x=3
x^=4
print(x)

print(bin(4))

#Comparison Operators
a=5
b=3
c=7
print(c<b<a)

print(a<b<c)

#Python does not suppport chained comparison and start evaluating from left to right , if any part becomes false and entire condition will false
print((a<b)==(a>=b))

#Logical operators
a=8
b=7
print((a<b and b<a))

print((a>b) or (a<=b))

print((a>b) and (a!=b))

print(not((a>b) or (a<b)))

#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
#SyntaxError: multiple statements found while compiling a single statement

#performs the execution based on the location
x=[1,2]
y=[1,2]
z=[2,1]
print(x is y)
print(x is z)
#Same content but different memory locator return false
z=x
print(x is z)
True
# point to the same location
print( x is not y)
True
list =[1,3,4,5]
print( 1 in list)
True
print( 1 ,4 in list)

True


#Binary operators

print(bin(5))
print(bin(3))
print(bin(6))
print(bin(3))

print(6&3)
2
print(6|3)
7
#Xor
print(6^3)
