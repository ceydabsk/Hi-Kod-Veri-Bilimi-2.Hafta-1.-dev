def faktoriyel(n):
    sonuc=1
    for i in range(1, n + 1):
        sonuc *= i

    return sonuc

sayi=int(input("Faktöriyel hesaplama için sayı giriniz:"))
fakt= faktoriyel(sayi)

print("Girilen {} sayısının faktöriyeli: {}".format(sayi,fakt))