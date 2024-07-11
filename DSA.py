import numpy as np

twoDArray=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]])
print(twoDArray)

newTwoDArry=np.delete(twoDArray,0 ,axis=1)
print(newTwoDArry)

def searchTwoDArray(array,value):
    for i in range (len(array)):
        for j in range (len(array[0])):
            if array[i][j]==value:
                return "the value is located at: "+str(i)+" " +str(j)
            
    return "value not found"

print(searchTwoDArray(twoDArray,255))        

def searchTwoDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return f"The value is located at: {i} {j}"
    return "Value not found"

def createTwoDArray():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    array = []
    
    for i in range(rows):
        row = []
        print(f"Enter values for row {i + 1}, separated by spaces:")
        row_values = input().split()
        if len(row_values) != cols:
            print(f"Error: You must enter exactly {cols} values.")
            return createTwoDArray()
        for value in row_values:
            row.append(int(value))
        array.append(row)
    
    return array

# Get user input for the 2D array
print("Create your 2D array:")
twoDArray = createTwoDArray()
print("Your 2D Array:")
for array in twoDArray:
    print(array)

# Get user input for the value to search
search_value = int(input("Enter the value to search for: "))

# Search for the value in the 2D array
print(searchTwoDArray(twoDArray, search_value))

