def indirim_hesapla():
    fiyat = float(input("Ürünün fiyatı nedir?: "))
    indirim = float(input("İndirim oranı nedir?: "))
    indirim_miktari = fiyat * (indirim / 100)
    yeni_fiyat = fiyat - indirim_miktari
    print(f"İndirimli fiyat {yeni_fiyat} TL dir")
    print(f"İndirim miktarı {indirim_miktari} TL dir")
indirim_hesapla()