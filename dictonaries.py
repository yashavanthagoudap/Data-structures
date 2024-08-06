## Dictonaries:- "A dictonary is a collection which is unordered,changeable and indexed "

# Creating dictonary 
my_dict=dict() ## TIME COMPLEXITY:O(1) ## SPACE COMPLEXITY: O(1)
print(my_dict)

my_dict2={} ## TIME COMPLEXITY:O(1) ## SPACE COMPLEXITY: O(1)
print(my_dict2)

eng_kan=dict(one='ondu',two='eradu',three='muru')
print(eng_kan)

eng_kan1={'one':'ondu','two':'eradu','three':'muru'}
print(eng_kan1)

## UPDATE/EDIT EXISTING DITIONARY
my_dict={'name':'yash','age':23}
my_dict['place']='uk'
print(my_dict)

## TRAVERSING THROUGH A DICTONARY

my_dict={'name':'yash','age':23,'address':'londan'}

def dictTraverse(dict):
    for key in dict:
        print(key , dict[key])
dictTraverse(my_dict)         

## Finding the value for Dictonary through LINEAR SEARCH

my_dict={'name':'yash','age':23,'address':'londan'}

def searchDict(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value
    return 'Valuve doenot exist'   

print(searchDict(my_dict,23)) 

## Deleting element from dictonary

my_dict={'name':'yash','age':23,'address':'londan','education':'graduvate'}

del my_dict['age']
removed_element=my_dict.pop('name')
removed_element=my_dict.popitem()
print(removed_element)
my_dict.clear()
print(my_dict)

## Dictonary Method
my_dict={'name':'yash','age':28,'address':'londan','education':'graduvate'}

## 1. claer() 2. copy() 3. fromkeys() dictonary.fromkeys(sequence[],value) 4. get()  doctonary.get(key,value)
## 5. items() 6. keys() 7. popitem() 8. setdefault() dictonary.setdefault(key,default_value) 9. pop() dictonary.pop(key,default_value)
## 10. values() 11. update() dictonary.update(new_dictonary)


new_dict={}.fromkeys([1,2,3],9)
print(new_dict)

print(my_dict.get('age',21))
print(my_dict.items())
print(my_dict.keys())
print(my_dict.popitem())
print(my_dict)

print(my_dict.setdefault('name1','added'))
print(my_dict)

print(my_dict.pop('name1','not'))
print(my_dict.values())

new_dict={'a':1,'b':2,'c':3}
my_dict.update(new_dict)
print(my_dict)

## Builtin functions
# 1. len() 2. all() 3. any() 4. sorted()

print(all(my_dict))
print(sorted(my_dict))

import random
city_names={'gadag','bengaluru','hubbli','dvg'}

city_temp={city:random.randint(20,40) for city in city_names}
print(city_temp)

city_temp1={city:temp for (city,temp) in city_temp.items() if temp>25}
print(city_temp1)