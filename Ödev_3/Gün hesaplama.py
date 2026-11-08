import datetime
simdi = datetime.datetime.now()
tarih = input("Lütfen tarihi giriniz (YYYY-MM-DD): ")
sonuc = datetime.datetime.strptime(tarih, "%Y-%m-%d")
fark = (sonuc - simdi)
print(f"Girdiğiniz tarih ile şu anki tarih arasındaki fark: {fark.days} gün,{fark.seconds // 3600} saat kaldı.")

