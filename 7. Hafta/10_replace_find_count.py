# Üzerinde farklı metotların uygulanacağı bir metin oluşturur.
metin = "python programlama python"

# Metindeki bütün "python" parçalarını "Python" ile değiştirir ve yeni değer oluşturur.
yeni = metin.replace("python", "Python")

# "programlama" kelimesinin başladığı indeksi bulur.
konum = metin.find("programlama")

# "python" kelimesinin metinde kaç kez geçtiğini hesaplar.
adet = metin.count("python")

# Değiştirilmiş yeni metni ekrana yazdırır.
print(yeni)

# Bulunan başlangıç indeksini ekrana yazdırır.
print(f"Konum: {konum}")

# Tekrar sayısını ekrana yazdırır.
print(f"Adet: {adet}")
