"""
def union(self, other):
        # Return the union of two sets as a new set.
        
def intersection(self, other):
        # Return the intersection of two sets as a new set.
        
def difference(self, other):
        # Return the difference of two sets as a new set.

def symmetric_difference(self, other):
        # Return the symmetric difference of two sets as a new set.
        
def remove(self, element):
        # Remove an element from a set; it must be a member.
        
def disjoint(self, other):
        # Return True if two sets have a null intersection.
        
def issubset(self, other):
        # Report whether another set contains this set.

collections used for storing and organizing many values (objects) in one place instead creating multiple variable

def issuperset(self, other):
        # Report whether this set contains another set.
        
def update(self, *others):
        # Update a set with the union of itself and others.
        
# add 

"""


#set

## set : unordered collection of unique objects
# mutable
# defined by curly braces {} or set()
# set() - empty set
# set - iterable
# set - no indexing, slicing, dicing
# set - no duplicate values

# st ={10,"hai",True,10,"hai"}

# print(st[0]) # TypeError: 'set' object is not subscriptable

# print(st)

st1={10,20,30,40}

st2={100,10,200,20,300,30}

union_set = st1.union(st2) #st1 | st2
print("union:",union_set)

intersection_set = st1.intersection(st2) # st1 & st2
print("intersection:",intersection_set)

difference_set = st1.difference(st2) # st1 - st2
print("difference:",difference_set)