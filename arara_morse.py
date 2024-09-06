encode_morse = {'a':'.-', 'r':'.-.'}
decode_morse = {v: k for k, v in encode_morse.items()}

def codifica(palavra):
    saida = ""
    for char in palavra:
        try:
            saida += encode_morse[char] + " "
        except KeyError:
            saida += "?" + " "
    return saida

def decodifica(morse):
    saida=""
    for l in morse.split(" "):
        try:
            saida += decode_morse[l]
        except KeyError:
            saida += "?"
    return saida

##Main
palavras = ["arara","araras","arar","rara","rar"]
for p in palavras:
    morse = codifica(p).strip()
    print(morse)
    print(decodifica(morse)+'\n')