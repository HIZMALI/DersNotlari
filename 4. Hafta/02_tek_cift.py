# Kullanıcıdan kontrol edilecek tam sayıyı alır.
sayi = int(input("Bir tam sayı girin: "))

# Sayının 2 ile bölümünden kalan sıfırsa sayının çift olduğunu belirler.
if sayi % 2 == 0:
    # Koşul doğruysa çift sayı mesajını gösterir.
    print("Sayı çifttir.")
else:
    # Koşul yanlışsa geriye tek sayı olma durumu kaldığı için bu mesajı gösterir.
    print("Sayı tektir.")
