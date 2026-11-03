# Döngüyü 1'den 5'e kadar çalıştırarak beş not alınmasını sağlar.
for sira in range(1, 6):
    # Her turda kullanıcıdan bir not alır ve tam sayıya dönüştürür.
    notu = int(input(f"{sira}. not: "))
    # Girilen notu sıra numarasıyla birlikte ekrana yazar.
    print(f"{sira}. not olarak {notu} girildi.")
