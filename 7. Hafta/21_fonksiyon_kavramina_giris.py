# Ekrana sabit bir ayraç çizgisi yazan fonksiyonu tanımlar.
def cizgi_yaz():
    # Fonksiyon her çağrıldığında 30 tire karakteri yazdırır.
    print("-" * 30)

# Rapor başlığını ekrana yazdırır.
print("METİN RAPORU")

# Daha önce tanımlanan ayraç fonksiyonunu çağırır.
cizgi_yaz()

# Örnek rapor satırını ekrana yazdırır.
print("İşlem tamamlandı.")

# Aynı fonksiyonu tekrar çağırarak kodun yeniden kullanılabildiğini gösterir.
cizgi_yaz()
