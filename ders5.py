import requests
from bs4 import BeautifulSoup
import csv
import time # Siteye çok hızlı yüklenip ban yememek için "bekleme" modülü

# Dosyamızı hazırlayalım
dosya = open("tum_kitaplar.csv", "w", encoding="utf-8", newline="")
kalem = csv.writer(dosya)
kalem.writerow(["Kitap Adı", "Fiyat", "Sayfa No"]) # Hangi sayfadan geldiğini de yazalım

# --- ANA DÖNGÜ: SAYFALARI GEZMEK ---
# range(1, 6) demek: 1'den başla, 6'ya KADAR (6 dahil değil) git. Yani 1,2,3,4,5. sayfa.
for sayfa_no in range(1, 6):
    
    # URL'yi dinamik olarak oluşturuyoruz.
    # f"..." yapısı sayesinde {sayfa_no} kısmı her turda değişecek (1, 2, 3...)
    url = f"http://books.toscrape.com/catalogue/page-{sayfa_no}.html"
    
    print(f"--> Şu an {sayfa_no}. sayfa taranıyor: {url}")
    
    # Siteye bağlan
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # O sayfadaki 20 kitabı bul
    kitaplar = soup.find_all("article", class_="product_pod")
    
    # --- ALT DÖNGÜ: KİTAPLARI TOPLAMAK ---
    for kitap in kitaplar:
        baslik = kitap.find("h3").find("a")["title"]
        fiyat = kitap.find("p", class_="price_color").text
        
        # Dosyaya kaydet (Sayfa numarasını da ekledik)
        kalem.writerow([baslik, fiyat, sayfa_no])
        
    print(f"    {len(kitaplar)} adet kitap kaydedildi.")
    
    # Robot olduğumuz anlaşılmasın diye her sayfadan sonra 1 saniye bekleyelim
    time.sleep(1)

# Her şey bitince dosyayı kapat
dosya.close()
print("------------------------------------------------")
print("TÜM İŞLEM BİTTİ! 'tum_kitaplar.csv' dosyana bakabilirsin.")