 # a LIST is a data structure that holds an ordered collection of items
# ex:
# integer_list=[1,2,3]
# string_list=['yash','a','patil']
# list=[1,2,0.35,'sir',[78,'ram',778.34]]

## Creating list
# integer_list=[1,2,3]
# print(integer_list)

# string_list=['yash','a','patil']
# print(string_list)

# list=[1,2,0.35,'sir',[78,'ram',778.34]]
# print(list)

# empty_list=[]
# print(empty_list)

##
#Accessing list/Traversing
# shoping_list=['milk','soap','dress']
# print(shoping_list[0])
# print(shoping_list[-2])
# print('milk' in shoping_list)

# print("++++++++")
# for i in shoping_list:
#     print(i)

# print("++++++++")
# for i in range (len(shoping_list)):
#     shoping_list[i]=shoping_list[i]+ " " +'XXXX'
#     print(shoping_list[i])

# print("++++++++")
# empty=[]
# print("kjb")
# for i in empty:
#     print("i am empty")
#     print ("liksbg")
 ##

#Update/insert list

# myList=[1,2,3,4,5,6,7,8]
# print(myList)
# # myList[2]=33
# # myList[4]=55
# # print(myList)

# #insert method:inserting the element at any given index
# # myList.insert(0,11)
# # print(myList)
# # myList.insert(4,14)
# # print(myList)

# #Appand method:insert the element at the end of the list
# # myList.append(99)
# # print(myList)

# #Extend method:Adding the new list to the existing list
# newList=[11,12,13,14]
# myList.extend(newList)
# print(myList)

##Delete/Slice

# myList=[1,2,3,4,5,6,7,8]
# print(myList)
# myList[0:2]=['x','y']
# print(myList[0:])

#POP method:delete the element through the index or
#      if you are not providede the index it will delete the last element
# print(myList.pop())  
# print(myList)

#DELETE method:delete the element through the index
# del myList[:-1]
# print(myList)

##Remove method:it will delete/remove the direct providede value

# myList.remove(1)
# print(myList)

## SEARCHING element in the list
# my_list=[10,20,30,40,50,60,70,80,90]

# target=50

## IN OPERATOR
# if target in my_list:
#     print(f"{target} is in the list")
# else:
#     print(f"{target} is not in the list")    

## LINEAR SEARCH

# def linear_search(p_list,p_target):
#     for i,value in enumerate(p_list):
#         if value==p_target:
#             return i
#     return -1

# print(linear_search(my_list,target))    

## LIST OPERATIOR ?FUNCTION

# a=[1,2,3] 
# b=[4,5,6,22]
# # c=a+b ## '+' Operator 

# a=[1,4]
# a=a*5  '*' Operator
## len():Return the number of elements inside list
# a=[1,2,3,4,5,5,6,7,78,8] 
# print(len(a))
## MAX():returns the item with highest value in the list 
# print(max(a))
## MIN():returns the item with lowest value in the list 
# print(min(a))
##SUM():return the sum of the items in the list
# print(sum(a))
# print(sum(a)/len(a))

# my_list=list()
# while(True):
#     inp = input('enter a number: ')
#     if inp == 'done':break
#     value=float(inp)
#     my_list.append(value)
# avg=sum(my_list)/len(my_list)

# print('AVARAGE: ',avg)

 ## CONVERTING STRING TO LIST 

str = 'spam'
my_list=list(str)
print(my_list)

str = 'spam list spam'
my_list =str.split()
print(my_list)