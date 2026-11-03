# Kullanıcıdan ilk puan değerini alır.
puan = int(input("Puan: "))

# Puan 0 ile 100 aralığında olmadığı sürece tekrar eder.
while not (0 <= puan <= 100):
    # Kullanıcıya geçersiz değer girdiğini bildirir.
    print("Puan 0 ile 100 arasında olmalıdır.")
    # Kullanıcıdan yeni bir puan değeri alır.
    puan = int(input("Puan: "))

# Geçerli puanın kaydedildiğini bildirir.
print("Puan kaydedildi:", puan)
