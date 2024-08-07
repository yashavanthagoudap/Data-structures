# TUPLE: A tuple is an immutable sequence of python objects
# Tuples are also comparable and hashable
# ex:
t=('a','b','patil','sir')
tt='a','b','c','d'
ttt=('a',)  ## Time compexity:O(1) , Space complexity:O(n)
t_t=tuple('argdf')
print(tt[-1])
print(tt[1:3])

## HOW TO TRAVERSE THROUGH TUPLE

Tuple=('a','b','s','g','q','l')

for i in Tuple:
    print(i)

for i in range (len(Tuple)): ## Time compexity:O(n) , Space complexity:O(1)
    print(Tuple[i])

print('f' in Tuple)  ## Time compexity:O(n)
print(Tuple.index('l'))  ## Time compexity:O(n)

def searchElement(new_tuple,element):
    for i in range(0,len(new_tuple)):   ## Time compexity:O(n)
        if new_tuple[i]==element:
            return f"the {element} present in the index of {i}"
    return f"the element '{element}' is not found"    
print(searchElement(Tuple,'x'))        

#  Operations/functions
myTuple=(1,2,3,5,4,5)
myTuple1=(5,6,7,8,9)

print(myTuple+myTuple1)
print(myTuple *4)
print(9 in myTuple)
print(myTuple.count(5))
print(myTuple.index(5))
print(len(myTuple))
print(max(myTuple1))
print(min(myTuple1))
print(tuple([4,2,44,5,5,6,7,8]))