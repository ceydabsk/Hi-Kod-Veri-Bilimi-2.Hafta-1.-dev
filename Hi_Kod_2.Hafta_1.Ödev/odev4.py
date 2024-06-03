from datetime import datetime

def emeklilik_hesaplama(yas):
    if yas<65:
        emeklilik_yil=65-yas
        print(f"{isim},emekliliğe {emeklilik_yil} yılınız kaldı!")
    elif yas>=65:
        print("Emekli oldunuz!")

def yas_hesaplama(dogum_yili):
    bugun = datetime.now()
    bugun_yil = bugun.year
    yas= (bugun_yil-dogum_yili)
    return yas

isim=input("İsminiz:")
dogum_yili = int(input("Doğum yılınızı giriniz:"))
sonuc = emeklilik_hesaplama(yas_hesaplama(dogum_yili))
