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