# given string of spaced separate words return longest word.
#


#split
#len()
#sort by len()

text = "red white blue violet dfgdfgdfgdfgfdgdf aaeaeaeea"
words = text.split()

res = words[0]
for w in words:
    if len(w) >= len(res):
        res = w
    
print(res)

