#How to add an elemet to a list
List =[1,3,4,5,6,7,8,9]
print(List.append(1))
#my_list[] = 1
#my_list.extend(1)
#my_list.push(1)


#How to access the first element from the list
print(List[0])
#my_list.get(0)
print(List[0:])
#my_list[0:]
#my_list[1]

#How to we calculate the length of list
print([len(List)])


#How do you access the last element of a list?
print("The last element is " ,List[-1])
#pop(my_list)
#my_list.get(-1)


#How do you remove the last element from a list?
print(List.pop())
#pop(List)
#my_list[-1] = None

#How to check something in in list
if 1   in List:
 print("a is not in b")
 print(List.sort())
 sorted(List)
 #List = sort(List)
 #sort(my_list)

 if 6 in List:
     List.remove(6)
     print(List)