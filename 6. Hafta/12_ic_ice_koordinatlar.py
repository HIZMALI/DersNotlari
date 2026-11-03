# x değerini 1'den 3'e kadar ilerleten dış döngüyü başlatır.
for x in range(1, 4):
    # Her x değeri için y değerini 1'den 2'ye kadar ilerletir.
    for y in range(1, 3):
        # O anda oluşan x ve y değerlerini koordinat biçiminde gösterir.
        print(f"({x}, {y})")
