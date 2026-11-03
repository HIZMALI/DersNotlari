# Kullanıcıdan yaş bilgisini tam sayı olarak alır.
yas = int(input("Yaş: "))

# Negatif yaş değerlerini geçersiz kabul eder.
if yas < 0:
    # Geçersiz yaş için hata mesajı gösterir.
    print("Geçersiz yaş.")
elif yas <= 12:
    # 0 ile 12 arasındaki yaşları çocuk grubuna atar.
    print("Yaş grubu: Çocuk")
elif yas <= 17:
    # 13 ile 17 arasındaki yaşları ergen grubuna atar.
    print("Yaş grubu: Ergen")
elif yas <= 64:
    # 18 ile 64 arasındaki yaşları yetişkin grubuna atar.
    print("Yaş grubu: Yetişkin")
else:
    # 65 ve üzerindeki yaşları ileri yaş grubuna atar.
    print("Yaş grubu: İleri yaş")
