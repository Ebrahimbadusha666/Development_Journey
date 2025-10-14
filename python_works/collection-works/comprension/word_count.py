
word=["hai","hello","goodmorning","hai","goodevening","hello","hai"]

# word_count= {}

# for w in word:
    
#     if w in word_count:
        
#         word_count[w]+=1
        
#     else:
        
#         word_count[w]=1
        
# print(word.count("hai"))

word_count={w:word.count(w) for w in word}

print(word_count)