

years= [1899,1900,2000,2021,2022,2023,1991,1992]

# century_years_list
# non_centry_years_list

century_years_list=[]

non_centry_years_list=[]

for year in years:
    
    if year%100==0:
        
        century_years_list.append(year)
        
    else:
        
        non_centry_years_list.append(year)

print("century years:",century_years_list)

print("non century years:",non_centry_years_list)
