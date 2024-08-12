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
        # if value is not None:
        #     self.append(value)      
            
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node is not None:
                result += ' '
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

    def prepend(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node    # Time and space complexity: O(1)
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1  

    def insert(self, index, value):
        new_node=Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length==0:                # Time complexity: O(n) and space complexity: O(1)
            self.head=new_node
            self.tail=new_node
        elif index == 0:
            new_node.next=self.head
            self.head=new_node
        else:    
            temp_node=self.head
            for _ in range (index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length +=1    
        return True            

    def travers(self):
        current=self.head
        while current:                # Time complexity: O(n) and space complexity: O(1)
            print(current.value)
            current=current.next

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value ==target:
                return index            # Time complexity: O(n) and space complexity: O(1)
            current =current.next
            index += 1
        return -1

    

new_linked_list = LinkedList()
# new_linked_list.insert(0,90) 
new_linked_list.prepend(10)
new_linked_list.append(20)
new_linked_list.append(40)
new_linked_list.append(50)
print(new_linked_list)  
# new_linked_list.insert(-2,90) 
# print(new_linked_list.travers()) 
print(new_linked_list.search(50))    