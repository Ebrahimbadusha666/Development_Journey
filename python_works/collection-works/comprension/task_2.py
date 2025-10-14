
words=["hai","hello","goodevening","hello","hai","goodmorning"]

# create a new words convert all words into uppercase

upper_words=[w.upper() for w in words]

print(upper_words)

# create a new dictionary from words set words as key and value as length

dic_wrds={w:len(w) for w in words}

print(dic_wrds)