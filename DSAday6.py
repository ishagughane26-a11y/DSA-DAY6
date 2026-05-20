#Reverse each word in string

# s="Hello World"
# words=s.split()

# for i in  range (len(words)):
#     words[i]= words[i][::-1]
# result=" ".join(words)

# print(result)


#check for valid parenthesis

# s ="({[()]})"

# stack = []
# valid =True
# for ch in s:
#     if ch =='(' or ch=='{' or ch =='[':
#         stack.append(ch)
#     else:
#         if len(stack)==0:
#             valid=False
#             break
#         top=stack.pop()

#         if ch==')' and top !='(':
#             valid=False

#         if ch=='}' and top !='{':
#             valid=False

#         if ch==']' and top !='[':
#             valid=False

# if len(stack) !=0:
#     valid=False

# if valid:
#     print("Valid")
# else:
#     print("Invalid")  


#Example  sort the List[5,3,8,6,2] in ascending order.
#Algorithm: DStart from the second element (index 1) because a single elemrnt is trivially sorted.
#Compare it with elememts before it and insert it in the coreect position.
#repeat this process for all elements.


#INSERTION SEARCH
# arr=[5,3,8,6,2]

# for i in range(1,len(arr)):
#     key=arr[i]
#     j=i-1

#     while j>=0 and  arr[j] > key:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=key
#     print(arr)
#     print()
# print(arr)    

#MUSCIS PLAYLIST
#Student mangement  using marks
#contact list

#Selection sort
# CPU SHEDULING                     

# arr = [20, 12, 10, 15, 2]

# for i in range(len(arr)):
#     min = i
#     j = i + 1

#     while j < len(arr):
#         if arr[j] < arr[min]:
#             min = j

#         j = j + 1
#     print(arr)
#     # swap
#     arr[i], arr[min] = arr[min], arr[i]
    
# print(arr)


#find all Duplicate in a list
#i/p={4,3,2,7,8,2,1,5,5}    o/p={2,5}

# arr=[4,3,2,7,8,2,1,5,5]

# duplicate=[]

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]  and arr[i] not in duplicate:
#            duplicate.append(arr[i])

# print(duplicate)

#Dictonary by key value
#i/p=("c":3,"B":2,"A":1)  output=assending order
# inp={"C":3,"B":2,"A":1}
# sort_dict=dict(sorted(inp.items()))
# print(sort_dict)
# mydict={"C":3,"B":2,"A":1}
# clr_dict=mydict.clear()
# print(mydict)


#TYPES OF VARIABLE
# class New:
#     def __init__(self):
#         self.a=10

# obj1 =New()
# obj2 =New()
# obj3 =New()  
# obj1.a=20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


# class New:
#     a=10

#     def __init__(self):
#         self.name="Isha"
# obj1 =New()
# obj2 =New()
# obj3 =New() 

# New.a=50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


#for every object a seprate copy of instance variable created but in case of static

#variable only one copy will be created and it is accessble for every object of the class

# class College:

#      collegename= "Modern College" #static variable (1 memory)

#      def __init__(self):

#       self.studentname = "prashant" #instance varible (3 seprate memory)

# principal = College() # object creation

# teacher = College()

# accountant = College()

# print("principal=", principal.collegename, "....", principal.studentname)

# print("teacher =", teacher.collegename, teacher.studentname)

# print("accountant=", accountant.collegename, "....", accountant.studentname)

# College.collegename="HBD" # second way to add static variable

# principal.studentname="prashant jha"

# print("principal=", principal.collegename, "|", principal.studentname)

# print("teacher =", teacher.collegename, "|", teacher.studentname)

# print("accountant=", accountant.collegename, "", accountant.studentname)

#LINKEDLIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def addNodeatBeg(self, data):

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def addNodeatEnd(self, data):

        self.addNode(data)

    # Add node in between
    def addNodeinBetween(self, data):

        pos = int(input("Enter position: "))

        new_node = Node(data)

        # Insert at beginning
        if pos == 1:

            new_node.next = self.head
            self.head = new_node

            if self.tail is None:
                self.tail = new_node

            return

        temp = self.head
        count = 1

        while temp is not None and count < pos - 1:

            temp = temp.next
            count += 1

        if temp is None:

            print("Position not found")

        else:

            new_node.next = temp.next
            temp.next = new_node

            if new_node.next is None:
                self.tail = new_node

    def display(self):

        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp is not None:

            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


if __name__ == '__main__':

    ll = LinkedList()

    while True:

        print('\n1. Add Node Linkedlist :')
        print('2. Add Node in Beginning :')
        print('3. Add Node in Between :')
        print('4. Add Node in End :')
        print('5. Display Linked List :')
        print('6. Exit')

        ch = int(input('Enter your choice :'))

        if ch == 1:

            value = int(input('Enter value for node: '))
            ll.addNode(value)
            print('Node added successfully.')

        elif ch == 2:

            value = int(input('Enter value for node: '))
            ll.addNodeatBeg(value)
            print('Node added successfully.')

        elif ch == 3:

            value = int(input('Enter value for node: '))
            ll.addNodeinBetween(value)
            print('Node added successfully.')

        elif ch == 4:

            value = int(input('Enter value for node: '))
            ll.addNodeatEnd(value)
            print('Node added successfully.')

        elif ch == 5:

            ll.display()

        elif ch == 6:

            break

        else:

            print('Invalid choice')