# Kontrol edilecek dosya adını kullanıcıdan alır.
dosya = input("Dosya adı: ").strip()

# Dosya adını küçük harfe dönüştürerek .pdf ile bitip bitmediğini kontrol eder.
pdf_mi = dosya.lower().endswith(".pdf")

# Dosya adının rapor kelimesiyle başlayıp başlamadığını kontrol eder.
rapor_mu = dosya.lower().startswith("rapor")

# PDF kontrolünün sonucunu ekrana yazdırır.
print(f"PDF mi? {pdf_mi}")

# Başlangıç kontrolünün sonucunu ekrana yazdırır.
print(f"Rapor ile başlıyor mu? {rapor_mu}")
