
shirts = [
  { "id": 1, "title": "Classic White Shirt", "brand": "Allen Solly", "price": 1499, "sizes": ["S", "M", "L", "XL"] },
  { "id": 2, "title": "Slim Fit Denim Shirt", "brand": "Levi's", "price": 2299, "sizes": ["M", "L", "XL"] },
  { "id": 3, "title": "Casual Checked Shirt", "brand": "U.S. Polo Assn.", "price": 1799, "sizes": ["S", "M", "L"] },
  { "id": 4, "title": "Formal Blue Shirt", "brand": "Van Heusen", "price": 1999, "sizes": ["M", "L", "XL", "XXL"] },
  { "id": 5, "title": "Printed Cotton Shirt", "brand": "Flying Machine", "price": 1299, "sizes": ["S", "M", "L"] },
  { "id": 6, "title": "Black Party Shirt", "brand": "Peter England", "price": 1599, "sizes": ["M", "L", "XL"] },
  { "id": 7, "title": "Linen Striped Shirt", "brand": "Raymond", "price": 2499, "sizes": ["S", "M", "L", "XL"] },
  { "id": 8, "title": "Half Sleeve Polo Shirt", "brand": "Tommy Hilfiger", "price": 2699, "sizes": ["M", "L"] },
  { "id": 9, "title": "Checked Flannel Shirt", "brand": "H&M", "price": 1399, "sizes": ["S", "M", "L", "XL"] },
  { "id": 10, "title": "Casual Printed Shirt", "brand": "Zara", "price": 1899, "sizes": ["S", "M", "L", "XL"] }
]

# display all shirt titles

all_shirt_titles=[s.get("title") for s in shirts]
print("All shirt titles: ", all_shirt_titles)

# display all shirt size

all_shirt_sizes=set(size for shirt in shirts for size in shirt.get("sizes"))
print("All shirt sizes: ", all_shirt_sizes)

# display shirts whos prize>150

shirts_gt_150=[shirt.get("title") for shirt in shirts if shirt.get("price") >1500]
print("Shirts with price > 1500: ", shirts_gt_150)

# display shirts available in size S
shirts_size_s=[shirt.get("title") for shirt in shirts if "S" in shirt.get("sizes")]
print("Shirts available in size S: ", shirts_size_s)

# display brands where price>1500 and size not available in XL

brands_price_gt_1500_no_xl=[shirt.get("brand") for shirt in shirts if shirt.get("price") >1500 and "XL" not in shirt.get("sizes")]
print("Brands with price > 1500 and size XL not available: ", brands_price_gt_1500_no_xl,"\n")

# display costly shirt
max_price=max(shirt.get("price") for shirt in shirts)
print("Costliest shirt price: ", max_price)
costly_shirt=[shirt.get("title") for shirt in shirts if shirt.get("price")==max_price]
print("Costliest shirt: ",costly_shirt,"\n")

#display size along with count of shirts
all_sizes=[size for shirt in shirts for size in shirt.get("sizes")]
size_count={size:all_sizes.count(size) for size in all_sizes}
print("Size count: ", size_count)

# 
