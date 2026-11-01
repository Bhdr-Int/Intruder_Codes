def harf_notu_hesapla():
    vize = int(input("Vize notunuzu giriniz: "))
    final = int(input("Final notunuzu giriniz : "))
    sonuç = (vize * 0.4) + (final * 0.6)
    if sonuç >= 90:
        print(f"Notunuz: {sonuç} AA")
    elif sonuç >= 85:
        print(f"Notunuz: {sonuç} BA")
    elif sonuç >= 80:
        print(f"Notunuz: {sonuç} BB")
    elif sonuç >= 75:
        print(f"Notunuz: {sonuç} CB")
    elif sonuç >= 70:
        print(f"Notunuz: {sonuç} CC")
    elif sonuç >= 65:
        print(f"Notunuz: {sonuç} DC")
    elif sonuç >= 60:
        print(f"Notunuz: {sonuç} DD")
    else:
        print(f"Notunuz: {sonuç} FF")
harf_notu_hesapla()
