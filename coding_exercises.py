# 1) MISSING NUMBER

def missing_number(arr,n):
    sum_of_number=(n*(n+1))//2

    sum_of_array=sum(arr)

    missing_number=sum_of_number-sum_of_array
    return missing_number

print(missing_number([1,2,3,4,6],6)) 

# 2) Finding pairs 

def findpairs(nums,target):
    for i in range (len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j]:
                continue
            elif nums[i]+ nums[j]==target:
                print(i,j)

myList=[1,2,3,2,3,4,5,6]
findpairs(myList,6)

# 3) How to check elemets in an array in Python

import numpy as np

myarry=np.array([1,2,3,4,5,6,22,7,8,9,10,23])

def findnumber(array,number):
    for i in range (len(array)):
        if array[i] == number:
            print("the element in the array is in the index of: ",i)

       
findnumber(myarry,2)


# 4) Max Product of Two Integers

def maxproduct(array):
    max1,max2=0,0

    for num in array:
        if num >max1:
            max2=max1
            max1=num

        elif num>max2:
            max2=num
    return max1 * max2 

arr=[1,7,3,4,9,5]
print(maxproduct(arr))            

# 5) MIDDLE FUNCTION (NEW LIST EXCEPECT THE FIRST AND LAST ELEMENT)

def newlist(list):
    return list[1:-1]

my_list=[1,2,3,4,5]

print (newlist(my_list))

## 6)SUM OF THE diagonaL MATRIX IN 2D Lists

def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0
 
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
 
    return total

my_list=[1,2,3] 

print(diagonal_sum(my_list))

## 7) first and seconde highest elemet in an list

def first_secone(my_list):
    max1,max2=float('-inf'),float('-inf')

    for num in my_list:
        if num>max1:
            max2=max1
            max1=num
        elif num>max2 and num !=max1:
            max2=num

    return max1,max2

my_list=[10,20,22,33,45,67,89,93]
print(first_secone(my_list))            