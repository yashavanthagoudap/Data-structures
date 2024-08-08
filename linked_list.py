## LINKED LIST:linked list is a form of sequential collection an it does not have to be order. 
## A linked list is made up of independent nodes that may contain any type of data and each node hase a reference to the next node in the link
## Ex: Train 1.Single linked list 2)Circular single linked list ex:4 palyers Chess board 3)Double linked list ex:Music 4)Circular double linked list ex:alt+tab 

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None     # Time and space complexity: O(1)

# new_node=Node(10)
# print(new_node)  

# class LinkedList:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.head=new_node         # Time and space complexity: O(1)
#         self.tail=new_node
#         self.length=1

class LinkedList:
    def __init__(self,value=None):
        self.head=None
        self.tail=None
        self.length=0 
        if value is not None:
            self.append(value)      
            
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node is not None:
                result += '-->'
                temp_node = temp_node.next
        return result         

    def append(self, value):
        new_node=Node(value)
        if self.head is None:             # Time and space complexity: O(1)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length += 1

    

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(40)
new_linked_list.append(50)
print(new_linked_list)        