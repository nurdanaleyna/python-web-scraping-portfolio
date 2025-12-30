import requests
from bs4 import BeautifulSoup
import csv  # <-- YENİ 1: CSV kütüphanesini çağırdık (Python'da hazırdır)

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

kitaplar = soup.find_all("article", class_="product_pod")

# --- YENİ 2: Dosyayı Oluşturma ---
# open("dosya_adi.csv", "mod", ayarlar)
# "w" = Write (Yazma modu). Dosya yoksa oluşturur, varsa içini silip baştan yazar.
# encoding="utf-8" = Türkçe karakterler (ş,ğ,ü) bozulmasın diye şart.
dosya = open("kitaplarim.csv", "w", encoding="utf-8", newline="")

# Dosyaya yazı yazacak "kalemi" hazırlıyoruz
kalem = csv.writer(dosya)

# İlk satıra Başlıkları (Sütun isimlerini) yazıyoruz
kalem.writerow(["Kitap Adı", "Fiyat"]) 

print("Veriler dosyaya yazılıyor...")

for kitap in kitaplar:
    baslik = kitap.find("h3").find("a")["title"]
    fiyat = kitap.find("p", class_="price_color").text
    
    # --- YENİ 3: Veriyi Dosyaya Kaydetme ---
    # print(baslik) yerine artık kalem.writerow() kullanıyoruz
    kalem.writerow([baslik, fiyat])

# Dosyayı kapatıyoruz (Bunu unutursan dosya boş kalır!)
dosya.close()

print("BİTTİ! 'kitaplarim.csv' dosyası oluşturuldu.")