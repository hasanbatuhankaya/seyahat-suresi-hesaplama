import pandas as pd

data = pd.read_excel("daata.xlsx",header=None)
iller = {
    "adana": 1,
    "adıyaman": 2,
    "afyonkarahisar": 3,
    "ağrı": 4,
    "amasya": 5,
    "ankara": 6,
    "antalya": 7,
    "artvin": 8,
    "aydın": 9,
    "balıkesir": 10,
    "bilecik": 11,
    "bingöl": 12,
    "bitlis": 13,
    "bolu": 14,
    "burdur": 15,
    "bursa": 16,
    "çanakkale": 17,
    "cankırı": 18,
    "çorum": 19,
    "denizli": 20,
    "diyarbakır": 21,
    "edirne": 22,
    "elazığ": 23,
    "erzincan": 24,
    "erzurum": 25,
    "eskişehir": 26,
    "gaziantep": 27,
    "giresun": 28,
    "gümüşhane": 29,
    "hakkari": 30,
    "hatay": 31,
    "ısparta": 32,
    "mersin": 33,
    "istanbul": 34,
    "izmir": 35,
    "kars": 36,
    "kastamonu": 37,
    "kayseri": 38,
    "kırklareli": 39,
    "kırşehir": 40,
    "kocaeli": 41,
    "konya": 42,
    "kütahya": 43,
    "malatya": 44,
    "manisa": 45,
    "kahramanmaraş": 46,
    "mardin": 47,
    "muğla": 48,
    "muş": 49,
    "nevşehir": 50,
    "niğde": 51,
    "ordu": 52,
    "rize": 53,
    "sakarya": 54,
    "samsun": 55,
    "siirt": 56,
    "sinop": 57,
    "sivas": 58,
    "tekirdağ": 59,
    "tokat": 60,
    "trabzon": 61,
    "tunceli": 62,
    "şanlıurfa": 63,
    "uşak": 64,
    "van": 65,
    "yozgat": 66,
    "zonguldak": 67,
    "aksaray": 68,
    "bayburt": 69,
    "karaman": 70,
    "kırıkkale": 71,
    "batman": 72,
    "şırnak": 73,
    "bartın": 74,
    "ardahan": 75,
    "ığdır": 76,
    "yalova": 77,
    "karabük": 78,
    "kilis": 79,
    "osmaniye": 80,
    "düzce": 81,

}

il1 = input("Lütfen il ismini girin: ").lower()  
il2 = input("Lütfen il ismini girin: ").lower()  
hiz=int(input("Lütfen ortalama hızınızı giriniz:"))
cikis_saati_tam=int(input("Lütfen çıkacağınız saati giriniz(sadece tam saati örneğin 15.30da çıkacaksanız 15 giriniz dakika kısmını bir sonraki kısımda girmelisiniz):"))
cikis_saati_dk=int(input("lütfen çıkacağınız saatin dakika kısmını girin:"))
mola_durumu=int(input("Mola vermek istiyor musunuz?(Evet ise 1 hayır ise 2 ye basınız.)"))
mola_süresi=0
mola_süresi_saat=0
mola_süresi_dakika=0
if mola_durumu==1:
    mola_süresi=int(input("Lütfen mola vereceğiniz süreyi giriniz(Dakika cinsinden):"))
plaka_kodu1 = iller.get(il1)
plaka_kodu2 = iller.get(il2)
zaman=data[plaka_kodu1-1][plaka_kodu2-1]/hiz
zaman*=60 
zaman_saat=zaman/60
zaman_saat=int(zaman_saat)
zaman-=zaman_saat*60
zaman_dakika=zaman
if mola_süresi>=60:
    mola_süresi_saat=int(mola_süresi/60)
    mola_süresi_dakika=int(mola_süresi-(mola_süresi_saat*60))
else:
    mola_süresi_dakika=mola_süresi-(mola_süresi_saat*60)
varis_saat=cikis_saati_tam+zaman_saat+mola_süresi_saat
varis_dakika=cikis_saati_dk+zaman_dakika+mola_süresi_dakika
yol_km=data[plaka_kodu1-1][plaka_kodu2-1]
if varis_dakika>=60:
    varis_saat+=1
    varis_dakika-=60
for i in range(5):
    if varis_saat>24:
        varis_saat-=24

  
varis_dakika=int(varis_dakika)
zaman_dakika=int(zaman_dakika)
if varis_dakika<10:
    print(f"Yolunuz={yol_km} km,hedefe {zaman_saat} saat {zaman_dakika} dakikada varacaksınız,varış saatiniz-{varis_saat}:0{varis_dakika}")
else:
    print(f"Yolunuz={yol_km} km,hedefe {zaman_saat} saat {zaman_dakika} dakikada varacaksınız,varış saatiniz-{varis_saat}:{varis_dakika}")

    







