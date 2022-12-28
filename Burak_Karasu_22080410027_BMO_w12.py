sinav_sonuc = {"isimler":["Ayşe K.","Ahmet M.","Nuri C.", "Nawar T.", "Suzan T.", "Ala B."],#sinav_sonuc isimli sözlükte 'isimler' adlı anahtar kelime oluşturdum ve değerlerini girdim.
"Cinsiyet":["K","E","E","E","K","K"],#sözlüğe eklenen Öğrencilerin cinsiyetlerini girdim.
"Vize Notları":[80,60,77,25,36,75],#sözlüğe eklenen öğrencilerin vize notlarını girdim.
"Final Notları":[90,50,53,100,98,66],#sözlüğe eklenen öğrencilerin final notlarını girdim.
}

def KullaniciGirisi(): #Kullanicidan girdi alip, hesaplamadan sonra sonuçları Geçme Notlarına tanımlayacak fonksiyon oluşturdum.
    sinav_sonuc["Geçme Notları"]=[]#sözlüğe eklenen kullanıcıların Geçme notlarının sonradan hesaplanıp, 'Geçme Notları' adlı anahtar kelimesinde hafızada tutulabilmesi için, boş bir anahtar değer oluşturdum. 
    for j in range(len(sinav_sonuc["Final Notları"])):#final notları içinde dolanabilmek için döngü başlattım
        gecmenotu1 = int(sinav_sonuc["Final Notları"][j]*(70/100) + sinav_sonuc["Vize Notları"][j]*(30/100)) #geçme notunu bilgisayara tanıttım ve işlem yaptırdım.
        if gecmenotu1 < 60:
            sinav_sonuc["Geçme Notları"].append("Kaldı: {}".format(gecmenotu1))#geçme notu 60'dan küçükse, notun önüne 'Kaldı' yazısını eklettirdim.
        else:
            sinav_sonuc["Geçme Notları"].append(gecmenotu1)#geçme notu 60'tan küçük değilse normal bir şekilde notu gecme notları adlı anahtar kelimeye ekledim.

    n = int(input("Kaç öğrenci ekleyeceğinizi giriniz : ")) #Kullanıcıdan kaç defa öğrenci bilgileri girişi yapacağının bilgisini aldım.
    print("------------------------")
    for i in range(1,n+1):# döngünün , 1'den kullanıcının girdiği sayıya kadar işlem yapmasını sağladım. (1,n+1) => 1 dahil ancak n+1 dahil değil. n dahil.
        isim = input("{}.ismi giriniz : ".format(i))#Kullanıcıdan isim bilgisini aldım.
        sinav_sonuc["isimler"].append(isim)#girilen bilgiyi isimler adlı anahtar kelimeye ekledim.
        cinsiyet = input("  cinsiyetinizi giriniz (K - E): ")#Cinsiyet bilgisini aldım.
        sinav_sonuc["Cinsiyet"].append(cinsiyet)#girilen bilgiyi cinsiyetler adlı anahtar kelimeye ekledim.
        vize =int(input("  vize notunuzu giriniz : "))#vize notu bilgisini aldım.
        sinav_sonuc["Vize Notları"].append(vize)#girilen bilgiyi Vize Notları adlı anahtar kelimeye ekledim.
        Final = int(input("  Final notunuzu giriniz :"))#final notu bilgisini aldım.
        sinav_sonuc["Final Notları"].append(Final)#girilen bilgiyi Final Notları adlı anahtar kelimeye ekledim.
        print("------------------------")
        
        gecmenotu2 = int(Final*70)/100 + int(vize*30)/100 #Sonradan girilen vize ve final notlarının hesabını yaptırdım.
        if gecmenotu2 < 60:
            sinav_sonuc["Geçme Notları"].append("Kaldı :{}".format(int(gecmenotu2)))#Eğer sonradan girilen verilerle geçmenotu 60'tan küçükse notun önüne 'kaldı' yazısı getirerek geçme notları adlı anahtar kelimeye ekledim.
        else:
            sinav_sonuc["Geçme Notları"].append(int(gecmenotu2))#geçme notu 60 tan küçük değilse normal bir şekilde ekledim.
print("------------------------")

KullaniciGirisi() #olusturdugum fonksiyonu cagırdım.
print(sinav_sonuc) #sözlüğün son halini ekrana yazdırdım.