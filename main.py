print("Internet Dil Sözlüğü'ne hoşgeldiniz")
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH":"Onaylamamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresiflesmek/Sinirlenmek",
            "YEET" : "Fırlatmak",
            "OOF" : "Durumun kötü olması",
            "ASDFGLNFDLKGJSDLNJKFG" : "Komik"
            }
while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!)(Çıkmak için EXİT yazın): ")
    if word!="EXİT":
        if word in meme_dict.keys():
            print(meme_dict[word])
        else:
            print("sözlükte bu kelime yok")
    else:
        break
print("Internet Dil Sözlüğü'nü kullandığınız için teşşekür ederiz")
