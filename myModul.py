

class Sifreleme:
    def __init__(self):
        print("Sifreleme sınıfı oluşturuldu.")
    
    def FernetEncrypt(self, veri):
        from cryptography.fernet import Fernet
        data = str.encode(veri) #string to bytes
        key=Fernet.generate_key()#şifreleme için anahtar üret.
        fernet=Fernet(key)
        encrypted=fernet.encrypt(data)
        return encrypted, key #Şifrelenmiş veriyi ve şifreleme anahtarını döndür.
    
    def FernetDecrypt(self, veri, key):
        from cryptography.fernet import Fernet
        fernet=Fernet(key)
        decrypted=fernet.decrypt(veri)
        return decrypted #çözülmüş veriyi döndürür.
    
    #--------------------------------------------------------
    #---Hashs----
    def shha256(self, metin):
        import hashlib
        result= hashlib.sha256(metin.encode())
        sifreli = result.hexdigest()
        return sifreli

    def md5(self, metin):
        import hashlib
        result = hashlib.md5(metin.encode())
        sifre= result.digest()
        return sifre

    def sha224(self, metin):
        import hashlib
        result = hashlib.sha224(metin.encode())
        sifre=result.hexdigest()
        return sifre

    def sha512(self, metin):
        import hashlib
        result = hashlib.sha512(metin.encode())
        sifre=result.hexdigest()
        return sifre

    def sha1(self, metin):
        import hashlib
        result = hashlib.sha1(metin.encode())
        sifre=result.hexdigest()
        return sifre



class dilKontrol():

    def __init__(self):
        print("dilKontrol sınıfı oluşturuldu.")
      
    def kelimeAyir(self,metin):
        import re
        ayirma = re.split("\s",metin)
        return ayirma

    def cumleAyir(self,metin):
        import re
        ayirma = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', metin)
        return ayirma

    def kelimesayma(self,metin):
        ayirma = self.kelimeAyir(metin)
        return len(ayirma)

    def cumlesayma(self,metin):
        ayirma = self.cumleAyir(metin)
        return len(ayirma)    

    def buyukUnluKontrol(self,metin):
        kalin_unluler = list("aıou")  # veya ['a', 'ı', 'o', 'u']
        ince_unluler = list("eiöü")  # veya ['e', 'i', 'ö', 'ü']
        liste=self.kelimeAyir(metin)
        sayacuyar=0
        sayacuymaz=0
        for kelimeler in liste:
               
                
            if (sum(kelimeler.count(kalin) for kalin in kalin_unluler)) != 0 and (sum(kelimeler.count(ince) for ince in ince_unluler)) != 0:  # Aynı kelime içerisinde hem kalın ünlü hem de ince ünlü bulunuyor mu diye bakar.
                sayacuyar=sayacuyar+1 
            else:
                sayacuymaz=sayacuymaz+1
        return sayacuyar,sayacuymaz        
            

    def sesliharf(self,metin):
    
        sesli_harf = 'AEIİOÖUÜaeıioöuü'
        sayac = 0
        for i in metin:
            if i in sesli_harf:
                sayac += 1
        return sayac


class Help:
    def __init__(self):
        print("""
            Class "dilKontrol"
            def kelimeAyir(self,metin): Gelen metni kelimelerine ayırıp geriye liste olarak döndürür.
            def cumleAyir(self,metin): Gelen metni cümlelerine ayırıp geriye liste olarak döndürür.
            def kelimesayma(self,metin): Gelen metindeki kelime sayısını döndürür.
            def cumlesayma(self,metin):Gelen metindeki cümle sayısını döndürür.
            def buyukUnluKontrol(self,metin): Gelen metini kelimelerine ayırır ve tek tek büyük ünlü uyumuna uyan ve uymayan kelimeleri bulup sayılarını geri dödürür.
            def sesliharf(self,metin): gelen metindeki sesli harf sayısını döndürür.
            """)
        print("""
            Class "Sifreleme"
            FernetEncrypt -> Parametre olarak verilen veriyi şifreler. Geriye şifreli veriyi ve şifreleme anahtarını döndürür.
            FernetDecrypt -> Parametre olarak şifreli veri ve anahtar alır. Anahtarla veriyi çözer geri döndürür.
            sha256 -> Parametre olarak verilen veriyi sha256 algoritmasıyla hashler.
            md5 -> Parametre olarak verilen veriyi md5 algoritmasıyla hashler.
            sha224 -> Parametre olarak verilen veriyi sha224 algoritmasıyla hashler.
            sha512 -> Parametre olarak verilen veriyi sha512 algoritmasıyla hashler.
            sha1 -> Parametre olarak verilen veriyi sha1 algoritmasıyla hashler.
            """)


