## 1) MISSING NUMBER

def missing_number(arr,n):
    sum_of_number=(n*(n+1))//2

    sum_of_array=sum(arr)

    missing_number=sum_of_number-sum_of_array
    return missing_number

print(missing_number([1,2,3,4,6],6)) 











