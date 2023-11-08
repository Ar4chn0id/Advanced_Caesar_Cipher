#metinde en çok geçen ve en az geçen harfi bul
#bu karakterleri rastgele 3 veya 2 sayıda olan karakter dizileri ile değiştir.(eğer en az geçen harfe denk gelmişse "1"veya"3" ve yanına 3 boyutunda rastgele karakterler, en çok geçen harfe denk gelmişse 0-9(1 ve 3 hariç) arasında rastgele bir sayı ve yanına 2 boyutunda rastgele karakterler gelecek. )
#geri kalan harfleri metinde bulunduğu konumun indexi tekse 5 eksiği kadar çiftse 6 fazlası kadar kaydır.
#anahtarı şifreli metnin başına ve sonuna ekle.(en çok bulunan karakter başa en az bulunan karakter sona)

import random

metin="Lorem ipsum dolor sit amet consectetur adipisicing elit. Obcaecati, porro? Quas reiciendis quo facilis vel unde hic! Obcaecati ipsa et in cum a ea quo iste, minima tenetur, aspernatur quas."

metin2="""Ne mutlu Türküm ağşçöm 

Diyene!!!"""

metin3="Bura Boyabat. Bakacağız!"
metin4="ABBCCCDDDEEEEE"

def Advanced_caesar_encrypt(text):

    def en_cok_en_az_karakterler(string):
        #excpt="!'^+%&/(\\)=?_<>£#$½{\n[]}\|`,.: ~´\"0123456789"
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
    #encryption_key = encok + enaz + replacement_characters_max + replacement_characters_min
    
    text=text.replace("ü","u").replace("ı","i").replace("ğ","g").replace("ö","o").replace("ş","s").replace("ç","c")
    print("şifrelenecek metin:",text)
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
            #*print("arttırma işlemi")
        else:
            if char == "1" or char == "3":
                dcrptxt += enaz
                ciphertxt = ciphertxt[:indexno+1] + ciphertxt[indexno + 4:]
                #*print("en az bulunan harf")
                indexno+=1
            else:
                dcrptxt += encok
                ciphertxt = ciphertxt[:indexno+1] +ciphertxt[indexno + 3:]
                #*print("en çok bulunan harf", indexno)
                indexno+=1
                #ciphertxt = ciphertxt[:indexno] + " " + ciphertxt[indexno:]
    return dcrptxt


cprtxt = Advanced_caesar_encrypt(metin4)
print("şifreli: ", cprtxt)
print("decrypt",Advanced_caesar_decrypt(cprtxt))



