"""
Last In First Out 

1. Creating
2. Inserting new elements
3. Deleting elements
4. Searching element
5. Sorting

"""

list1 = [1 ,3 , 5 , 2 , 10, 124, 53, 129]
stack1 = []

#creating
for i in list1:
    stack1.append(i)
    print (stack1)

#removing elements (last element)
stack1.pop()
print(stack1)
for i in range(0,len(stack1)):
    stack1.pop()
    print(stack1)
    