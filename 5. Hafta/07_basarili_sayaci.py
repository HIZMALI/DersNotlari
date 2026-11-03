# Kaç puan alındığını takip edecek sayacı sıfırlar.
adet = 0
# Başarılı puan sayısını sıfırlar.
basarili = 0

# Dört puan alınana kadar döngüyü sürdürür.
while adet < 4:
    # Kullanıcıdan bir sınav puanı alır.
    puan = int(input("Puan: "))
    # Puanın başarı sınırına ulaşıp ulaşmadığını kontrol eder.
    if puan >= 50:
        # Başarılı puan sayısını bir artırır.
        basarili += 1
    # Toplam giriş sayısını bir artırır.
    adet += 1

# Başarılı puanların kaç tane olduğunu gösterir.
print("Başarılı puan sayısı:", basarili)
