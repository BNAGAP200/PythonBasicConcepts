a = 10
b = 5
c = 1

if b < a:
    print(b < a)
elif a > b:
    print(a > b)
elif (b < c < a):
    print(b < a < c)

x = 3
y = 4
z = 2

if x != z:
    print(x != z)
else:
    print(x + y + z)

i = [10, 20, 13]
j = [20, 13, 9]

if 10 in i and 20 in i:
    print(i)

else:
    print(10 not in i)

L = (10.5, 21, 31, 78)
M = (1, 2, 3, 4, 5)

if all(item in M for item in L):
    print("All elements of tuple L are present in tuple M:" + L)

# Job requirements 1
education_level = "Bachelors degree"
years_of_experience = 5
str = input("What is your qualification :? ")

if education_level == "Bachelors,Masters":
    print("Proceed further ")
else:
    print("We looking for Bachelors degree, 12th pass candidate")

int = input("What is your level of expereince:? ")
if (years_of_experience <=3):
    print("Level up, wait for a update ")
else:
    print("Better luck next time")

# Job requirement 2

str = input("What is your qualification :? ")

if education_level == "Bachelors degree":
    if education_level.__contains__("Bachelor,Master,PG,12Th"):
        print("Proceed further ")

    int = input("What is your level of experience:?")
    if years_of_experience > 2:
        print("Your are level up and wait for further update")
    else:
        print("Sorry, better luck next time")
