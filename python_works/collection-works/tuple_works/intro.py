# tuple used for organizing and storing multiple valuesusing single varialble

# difine (), tuple()
# ordered, indexed, allow duplicate values
# immutable (not support item assignment, item deletion)

# tuple methods : count(), index()

"""
class tuple:

    def count(self,object) # return no.of occurence if object
    
    def index(self,object) # return first index position of object

"""

tp =(10,20,10,20)

freq= tp.count(10)
print(freq)

pos= tp.index(20)
print(pos)