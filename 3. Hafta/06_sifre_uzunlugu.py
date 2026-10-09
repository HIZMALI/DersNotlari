parola = input("Parola: ")  # Kullanıcıdan parola metnini alır.
uzunluk = len(parola)  # Parolanın kaç karakterden oluştuğunu hesaplar.
yeterli_uzunluk = uzunluk >= 8  # Parolanın en az sekiz karakter olup olmadığını kontrol eder.
print(f"Parola uzunluğu: {uzunluk}")  # Parolanın karakter sayısını ekrana yazar.
print(f"En az 8 karakter mi? {yeterli_uzunluk}")  # Uzunluk koşulunun True veya False sonucunu gösterir.
