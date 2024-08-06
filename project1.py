
## calculate the average temperature

numDays=int(input("How many day's temperature you want? "))
total=0
temp=[]
for i in range(numDays):
    nextDay=int(input("Day " + str(i+1) +"'s high temp:"))
    temp.append(nextDay)
    total +=temp[i]

avg=round(total/numDays,2)
print("\n Average = " + str(avg))    


above=0
for i in temp:
    if i > avg:
        above +=1

print(str(above) + " day(s) above average")        

# 2. Prime Number

def primeNumber(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count =count+1
    if count==2:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
num =int(input("plz enter a number:"))

primeNumber(num)
                     