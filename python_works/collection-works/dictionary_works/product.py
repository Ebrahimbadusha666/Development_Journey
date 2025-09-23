
# create dictionary product code,title,category,price,brand

product={
    "code":12354,
    "title":"laptop",
    "category":"gaming",
    "price":85000,
    "brand":"HP",
    "offer":100
}

# add key stock value 50 if not exist

if "stock" not in product:
    
    product["stock"]=50
    
# update offer a current offer+300 if offer exist else add offer as 250

if "offer" in product:
    
    product["offer"]+=300
    
else:
    
    product["offer"]=250
    
print(product)