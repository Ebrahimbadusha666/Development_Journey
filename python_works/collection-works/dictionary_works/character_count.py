
text = "abcdcdbcd"

# write a program to display character count

ch_count={}

for ch in text:
    
    if ch in ch_count:
        ch_count[ch]+=1
        
    else:
        
        ch_count[ch] =1
        
print(ch_count)

for k,v in ch_count.items():
    
    if v>1:
        
        print(k,v)
        
for k,v in ch_count.items():
    
    if v==1:
        
        print(k,v)
        
#dictionary methods

"""
def keys(self)
def values(self)
def items(self)
def get(self,key)
def pop(self,key)
def update(self)

"""