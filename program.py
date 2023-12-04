import random
import sys

ExampleText="Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati, porro? Quas reiciendis quo facilis vel unde hic! Obcaecati ipsa et in cum a ea quo iste, minima tenetur, aspernatur quas."

def Advanced_caesar_encrypt(text):

    def en_cok_en_az_karakterler(string):
        karakter_sayilari = {}
        
        for karakter in string:

            if karakter in karakter_sayilari:
                karakter_sayilari[karakter] += 1
            else:
                karakter_sayilari[karakter] = 1
        
        en_cok_karakter = max(karakter_sayilari, key=karakter_sayilari.get)
        en_az_karakter = min(karakter_sayilari, key=karakter_sayilari.get)
        
        return en_cok_karakter, en_az_karakter

    text=text.lower()
    excpt="!'^+%&/(\\)=?_<>£#$½{\n[]}\|`,.: ~´\"0123456789"
    for char in excpt:
        text=str(text).replace(char,"")
    sifrelimetin=""

    encok, enaz = en_cok_en_az_karakterler(text)
    
    text=text.replace("ü","u").replace("ı","i").replace("ğ","g").replace("ö","o").replace("ş","s").replace("ç","c")

    kaydirma_miktari=0
    for i in text:

        if i == encok:
            sifrelimetin+=f"{random.choice([0,2,4,5,6,7,8,9])}"+''.join([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(2)])
        elif i == enaz:
            sifrelimetin+=f"{random.choice([1, 3])}"+''.join([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3)])
        else:
            if kaydirma_miktari %2==0:
                shifted_char = chr(((ord(i) - ord('a') + kaydirma_miktari+6) % 26) + ord('a'))
                sifrelimetin+=shifted_char
            else:
                shifted_char = chr(((ord(i) - ord('a') + kaydirma_miktari-5) % 26) + ord('a'))
                sifrelimetin+=shifted_char

        kaydirma_miktari+=1
    ciphertext=encok+sifrelimetin+enaz
    return ciphertext

def Advanced_caesar_decrypt(ciphertxt):
    encok = str(ciphertxt)[0]
    enaz = str(ciphertxt)[-1]
    nums = "0123456789"
    dcrptxt = ""
    indexno = 0
    ciphertxt = str(ciphertxt)[1:-1]
    lencipher=len(ciphertxt)
    while indexno < lencipher:
        try: 
            char = ciphertxt[indexno]
        except IndexError:
            break
        if ciphertxt[indexno] not in nums:
            if (indexno) % 2 == 0:
                deshifted_char = chr(((ord(char) - ord('a') - indexno - 6) % 26) + ord('a'))
                dcrptxt += deshifted_char
            else:
                deshifted_char = chr(((ord(char) - ord('a') - indexno + 5) % 26) + ord('a'))
                dcrptxt += deshifted_char
            indexno += 1
        else:
            if char == "1" or char == "3":
                dcrptxt += enaz
                ciphertxt = ciphertxt[:indexno+1] + ciphertxt[indexno + 4:]
                indexno+=1
            else:
                dcrptxt += encok
                ciphertxt = ciphertxt[:indexno+1] +ciphertxt[indexno + 3:]
                indexno+=1
    return dcrptxt

flag = sys.argv[1]

if flag == "-e":
    with open(sys.argv[2], 'r') as file:
        userinput = file.read()
    with open('encrypted.txt', 'w') as file:
        file.write(Advanced_caesar_encrypt(userinput))
elif flag == "-d":
    with open(sys.argv[2], 'r') as file:
        userinput = file.read()
    with open('decrypted.txt', 'w') as file:
        file.write(Advanced_caesar_decrypt(userinput))
elif flag=="-h":
    print("Usage: program.py <flag> example.txt")
    print("flag: -e for encrypt, -d for decrypt" )
else:
    print("Wrong flag: -e for encrypt, -d for decrypt" )
    print("Usage: program.py <flag> example.txt")







