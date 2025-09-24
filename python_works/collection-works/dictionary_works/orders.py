
orders = ["tea","coffee","tea","coffee","coldcoffee","cappiciano","biriyani","biriyani"]

#first create an empyty dictionary

order_count = {}

#iterate  order

for o in orders : #o="tea"
    #chk o exist in order_count
    
    if o in order_count:
        
        #o exist in order_count
        #update o as current value+1 
        
        order_count[o]+=1 #update
        
    else:
        #o not exist in order_count
        order_count[o]=1
        
print(order_count)
