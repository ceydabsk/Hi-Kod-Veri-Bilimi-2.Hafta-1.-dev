from datetime import datetime


def yas_hesaplama(dogum_yili):
    bugun = datetime.now()
    bugun_yil = bugun.year
    yas= (bugun_yil-dogum_yili)
    return yas


dogum_yili = int(input("Doğum yılınızı giriniz:"))
sonuc = yas_hesaplama(dogum_yili)
print(f"{dogum_yili} yılında doğan {sonuc} yaşındadır.")
