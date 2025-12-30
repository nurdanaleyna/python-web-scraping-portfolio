import requests
from bs4 import BeautifulSoup  # Yeni kütüphanemizi çağırdık

url = "http://books.toscrape.com/"

# 1. Siteye bağlan ve veriyi al
response = requests.get(url)

if response.status_code == 200:
    # 2. Gelen karmaşık HTML'i BeautifulSoup ile "çorba" olmaktan çıkarıp düzenli hale getiriyoruz
    # "html.parser" parametresi, Python'a "bu bir HTML kodudur" dememizi sağlar.
    soup = BeautifulSoup(response.text, "html.parser")
    
    # --- GÖREV A: Sayfanın Başlığını Çek ---
    # HTML'deki <title> etiketini bul ve sadece metnini (.text) al
    sayfa_basligi = soup.find("title").text
    
    # --- GÖREV B: İlk Kitabın İsmini Çek ---
    # Sitede kitap isimleri <h3> etiketinin içindeki <a> etiketinde duruyor.
    # soup.find() komutu bulduğu İLK elemanı getirir.
    ilk_kitap = soup.find("h3").find("a")
    
    # "title" özelliğini (attribute) alıyoruz çünkü bazen isim uzunsa ekranda ... ile biter ama title içinde tam yazar.
    kitap_adi = ilk_kitap["title"]

    print("------------------------------------------------")
    print("SİTE BAŞLIĞI: " + sayfa_basligi.strip()) # .strip() baştaki/sondaki boşlukları siler
    print("İLK KİTAP:    " + kitap_adi)
    print("------------------------------------------------")

else:
    print("Siteye bağlanılamadı!")