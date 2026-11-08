import random

x = random.randint(1,100)

while True:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin ediniz: "))
    if tahmin < x:
        print("Daha büyük bir sayı tahmin ediniz.")
    elif tahmin > x:
        print("Daha küçük bir sayı tahmin ediniz.")
    else:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break


