import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# --- İŞTE SİHİR BURADA BAŞLIYOR ---

# 1. ADIM: Sayfadaki TÜM kitap kutularını buluyoruz.
# find_all komutu bize bir "Liste" verir. (kitaplar = [Kutu1, Kutu2, Kutu3...])
kitaplar = soup.find_all("article", class_="product_pod")

print(f"Bu sayfada toplam {len(kitaplar)} adet kitap bulundu.")
print("--------------------------------------------------")

# 2. ADIM: Döngü (Loop) başlatıyoruz.
# Türkçesi: "kitaplar listesindeki her bir 'kitap' için şunları yap:"
for kitap in kitaplar:
    
    # Başlığı bulma (Kutunun içindeki h3 -> a etiketine git)
    baslik_etiketi = kitap.find("h3").find("a")
    kitap_adi = baslik_etiketi["title"]
    
    # Fiyatı bulma (Kutunun içindeki p etiketine git)
    fiyat_etiketi = kitap.find("p", class_="price_color")
    fiyat = fiyat_etiketi.text
    
    # Ekrana yazdırma
    print(f"Kitap: {kitap_adi}")
    print(f"Fiyat: {fiyat}")
    print("---") # Karışmasın diye araya çizgi koyduk