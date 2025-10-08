
text = "BRUTE IS PLANNING TO KILL ME $$$"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = ""
key = --333

for letter in text.upper():
    if letter in alpha:
        letter_index = (alpha.find(letter) + key ) % len(alpha)
        cipher += alpha[letter_index]
    else:
        cipher += letter

print(cipher)

