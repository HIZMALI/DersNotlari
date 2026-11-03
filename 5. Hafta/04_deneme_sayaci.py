# Doğru PIN bilgisini saklar.
dogru_pin = "2468"
# Kullanıcının girişini başlangıçta boş metin olarak tanımlar.
giris = ""
# Deneme sayacını sıfırdan başlatır.
deneme = 0

# Kullanıcının girişi doğru PIN'den farklı olduğu sürece tekrar eder.
while giris != dogru_pin:
    # Kullanıcıdan yeni bir PIN değeri alır.
    giris = input("PIN: ")
    # Yapılan her giriş denemesini bir artırır.
    deneme += 1

# Doğru PIN girildiğinde başarı mesajını gösterir.
print("PIN doğru.")
# Toplam deneme sayısını ekrana yazdırır.
print("Deneme sayısı:", deneme)
