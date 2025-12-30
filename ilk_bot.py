import requests

# 1. Hedef site (Burası test için yapılmış sahte bir kitap sitesi)
url = "http://books.toscrape.com/"

# 2. Siteye "Bana sayfayı ver" diyoruz
cevap = requests.get(url)

# 3. Sonucu kontrol ediyoruz
if cevap.status_code == 200:
    print("------------------------------------------------")
    print("BAŞARILI! Siteye bağlandık.")
    print("Siteden gelen HTML kodunun ilk kısmı şöyle:")
    print("------------------------------------------------")
    print(cevap.text[0:300]) # İlk 300 karakteri yazdır
else:
    print("HATA! Bağlanamadık. Kod:", cevap.status_code)
    