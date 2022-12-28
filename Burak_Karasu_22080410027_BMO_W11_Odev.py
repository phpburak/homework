#sinav_sonuc adlı bir sözlük oluşturup içerisine ilk olarak isimler anahtar değerini oluşturup içerisine verileri girdim.
sinav_sonuc = {"isimler":["Ayşe K.","Ahmet M.","Nuri C.", "Nawar T.", "Suzan T.", "Ala B."]} 
#sinav_sonuc sözlüğüne cinsiyet anahtar değerini tanımlayıp verileri girdim.
sinav_sonuc["Cinsiyet"]="K","E","E","E","K","K"
#sözlüğe matematik notlarını tanımladım.
sinav_sonuc["Matematik Notları"]=80,60,77,25,36,75
#sözlüğe türkçe notlarını tanımladım.
sinav_sonuc["Türkçe Notları"]=90,50,53,100,98,66
print("\n") # 1 satır boşluk bırakarak daha rahat görünmesini sağladım.
print("İsimler : ",sinav_sonuc["isimler"]) #sinav_sonuc sözlüğüme atadığım isimler listesini yazdırdım.
print("\n")
print("Cinsiyetler: ",sinav_sonuc["Cinsiyet"]) #sözlüğe tanımladıgım cinsiyetler listesini yazdırdım.
print("Matematik notları : ",sinav_sonuc["Matematik Notları"]) #sözlüğe tanımladıgım matematik notlarımı yazdırdım.
print("Türkçe notları : ",sinav_sonuc["Türkçe Notları"]) #sözlüğe tanımladıgım türkçe notlarını yazdırdım.
print("\n")



KadinMatToplam = 0 #ortalama alabilmek için önce kadinlarin matematik notlarının toplamını bulabilmek için değeri 0'dan başlayan bir değer tanımladım.
ErkekMatToplam = 0 #ortalama alabilmek için önce erkeklerin matematik notlarının toplamını bulabilmek için değeri 0'dan başlayan bir değer tanımladım.
for i in range(len(sinav_sonuc["Matematik Notları"])): #döngünün tekrarını matematik notlarının eleman sayısı kadar olmasını sağladım.
    if sinav_sonuc["Cinsiyet"][i] == 'K': #Kadınların notlarını toplayabilmek için kadınların notları arasında sorgu yaptırarak, kadınların notlarını hafızaya aldım.
        KadinMatToplam = KadinMatToplam + sinav_sonuc["Matematik Notları"][i] #döngünün her tekrarında "KadinMatToplam" olarak atadığım değere kadınların notlarının eklenmesini sağladım.
    else: ErkekMatToplam = ErkekMatToplam + sinav_sonuc["Matematik Notları"][i] #if koşuluna giremeyen notlar erkeklerin notları toplamı olarak hafızada bekletiliyor.
print("kadinlarin matematik ortalamasi : ",KadinMatToplam/3) # kadınların toplam matematik notları, kadın sayısına bölünerek ortalama bulunur. Yazdırdım.
print("Erkeklerin matematik ortalamasi : ",ErkekMatToplam/3) # erkeklerin toplam matematik notları, erkeklerin sayısına bölünerek ortalama bulunur. Yazdırdım.



TurkceTop = 0 #Türkçe notlarının toplamının hafızada TurkceTop adlı int degerde saklanması için değeri sıfırdan başlatıp sonrasında notları bu değere ekleyeceğim.
for TurkceNotlari in sinav_sonuc["Türkçe Notları"]: #döngünün sözlükte türkçe notlarında dolaşmasını sağladım.
    TurkceTop = TurkceTop + TurkceNotlari #döngü her dönderdiğinde TurkceTop adlı değere türkçe notları ekledim.
print("Turkce Notlarının Sınıf Ortalaması : ",TurkceTop/6) #Türkçe not toplamını toplam sınıf mevcuduna bölerek ortalamayı yazdırdım.


#en yüksek değeri bulabilmek için kadınlar ve erkeklerin en yüksek türkçe notlarını ayrı listelerde tuttum.
kadinlarlist = [] 
erkeklerlist = []


for i in range(len(sinav_sonuc["Cinsiyet"])): #döngünün tekrar sayısını cinsiyetin eleman sayısı kadar belirledim.
    if sinav_sonuc["Cinsiyet"][i] == "K": #sadece kadınların turkce notlarında sorguyu sağladım.
        kadinlarlist.append(sinav_sonuc["Türkçe Notları"][i]) #cinsiyet K (Kadın) oldugu sürece türkçe notunu kadınlarlist adlı listeye ekledim
    else: erkeklerlist.append(sinav_sonuc["Türkçe Notları"][i]) #cinsiyet K değilse E dir E ye denk gelen notları da erkeklerlist adlı listeye ekledim.
print("\n")
print("Kadınların en yüksek Türkçe notu : ",max(kadinlarlist)) #kadinlarlist adli listenin max elemanını yazdırarak kadınların en yüksek notunu yazdırdım.
print("Erkeklerin en yüksek Türkçe notu : ",max(erkeklerlist)) #erkeklerlist adli listenin max elemanını yazdırarak erkeklerin en yüksek notunu yazdırdım.
print((sinav_sonuc))