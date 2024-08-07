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

## 8) Removing the Duplicates in a list

def remove_duplicates(lst):
    unique_lst=[]
    seen=set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst

my_list=[10,20,22,10,33,10,45,67,67,93,89,93]
print(remove_duplicates(my_list))        

## 9) Pairs of list is equal to targated value

def sum_pair(array,target):
    result=[]
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==target:
                result.append(f"{array[i]}+{array[j]}")
    return result

arr=[2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target=7
print(sum_pair(arr,target))            

## 10) Duplicates in an array True/False

def contains_duplicates(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return f"this array does not  contain duplicates element"

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,1]
print(contains_duplicates(nums))    

## 11) Permutations

def Permutations(lst1,lst2):
    if len(lst1) != len(lst2):
        return False
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        return True
    else:
        return False
    
lst1=[1,2,3] 
lst2=[2,3,1]
print(Permutations(lst1,lst2))   

## 12) Rotate the mtrix by 90 degree

def rotate(matrix):
    n = len(matrix)
 
    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 
    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate(matrix1))