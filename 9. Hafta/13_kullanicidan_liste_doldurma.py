# Kullanıcıdan alınacak notları saklamak için boş liste oluşturur.
notlar = []

# Beş kez veri girişi yapılmasını sağlayan döngüyü başlatır.
for _ in range(5):
    # Kullanıcıdan bir not alır ve tam sayıya dönüştürür.
    puan = int(input("Not: "))

    # Girilen notu listenin sonuna ekler.
    notlar.append(puan)

# Tamamlanan not listesini ekrana yazdırır.
print("Notlar:", notlar)
