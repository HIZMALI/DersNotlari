# Kullanıcıdan 0 ile 100 arasında olması beklenen puanı alır.
puan = int(input("Puan (0-100): "))

# Puan geçerli aralığın dışındaysa sınıflandırma yapmadan hata mesajı verir.
if puan < 0 or puan > 100:
    # Geçersiz puan değerini kullanıcıya bildirir.
    print("Hata: Puan 0-100 arasında olmalıdır.")
elif puan >= 85:
    # 85 ve üzerindeki geçerli puanları AA olarak sınıflandırır.
    print("Harf notu: AA")
elif puan >= 70:
    # 70 ile 84 arasındaki puanları BB olarak sınıflandırır.
    print("Harf notu: BB")
elif puan >= 50:
    # 50 ile 69 arasındaki puanları CC olarak sınıflandırır.
    print("Harf notu: CC")
else:
    # 0 ile 49 arasındaki geçerli puanları FF olarak sınıflandırır.
    print("Harf notu: FF")
