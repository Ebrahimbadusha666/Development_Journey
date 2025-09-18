
"""
class list:
    
    def append(self,object) # append object to end of the list object
    def insert(self,index,object) # add object at  specifiedindex
    def pop(self,index=-1) # remove and return item in specified index
    def index(self,object) # return first index of value
    def count(self,object) # return no.of occurence if object
    def reverse(self) #reverse the current list object
    def copy() # return shallow copy ofthe list
    def sort(self,reverse=False) # 
    def extend(self,iterable) # extend list by appending element from the iterable
    def remove(self,object) # remove first occurence of object

"""

colors=["red","blue","green","red","green","blue"]
#          0    1       2       3      4       5 

# colors.append("black")
# print(colors)

# colors.insert(2,"yellow")
# print(colors)

# colors.pop(2)
# print(colors)

# pos=colors.index("blue")
# print(pos)

# frequency = colors.count("red")
# print(frequency)

# colors.reverse()
# print(colors)

# colors_copy = colors.copy()
# print(colors_copy)

# expenses=[12000,15000,2000,25000,21000]
# expenses.sort(reverse=True) #asc
# # expenses.sort(reverse=False) #dec
# print(expenses)

# arr1=[10,20,30,40,]
# arr2=[100,200,300,400]
# arr2.extend(arr1)
# print(arr2)

colors.remove("blue")
print(colors)