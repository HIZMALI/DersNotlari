# Doğru PIN değerini saklar.
dogru_pin = "1234"
# Kullanıcının PIN girişini başlangıçta boş metin olarak tanımlar.
giris = ""
# Yapılan yanlış deneme sayısını sıfırlar.
deneme = 0

# PIN yanlış ve deneme sayısı üçten küçük olduğu sürece tekrar eder.
while giris != dogru_pin and deneme < 3:
    # Kullanıcıdan PIN girişini alır.
    giris = input("PIN: ")
    # Yapılan deneme sayısını bir artırır.
    deneme += 1

# Döngü sonunda girilen PIN'in doğru olup olmadığını kontrol eder.
if giris == dogru_pin:
    # Doğru PIN girildiyse erişim mesajını gösterir.
    print("Giriş başarılı.")
else:
    # Üç denemede doğru PIN girilemediyse kilit mesajını gösterir.
    print("Hesap kilitlendi.")

# Toplam deneme sayısını ekrana yazdırır.
print("Deneme sayısı:", deneme)
