text = 'werdwe wefdr we11daessafsdvdpiw jefpd'


vowels = 'aeuoai'

for char in text:
    if char.lower() not in vowels:
        text = text.replace(char, ".")

chains = text.split(".")
chains.sort(key=len)
print(text)
print(chains)