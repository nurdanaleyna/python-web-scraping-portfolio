# 📚 Kitap Veri Kazıma Botu (Web Scraping)

Bu proje, Python kullanarak geliştirdiğim ilk otomasyon projemdir. "Books to Scrape" sitesindeki kitap verilerini otomatik olarak çeker ve Excel (CSV) formatında kaydeder.

## 🎯 Projenin Amacı
Manuel olarak saatler sürecek veri toplama işlemini saniyeler içinde tamamlamak ve Python ile **Web Scraping / Veri Madenciliği** yetkinliklerimi göstermek.

## 🛠️ Kullandığım Teknolojiler
* **Python 3.12**
* **BeautifulSoup4:** HTML ayrıştırma ve veri çekme işlemi için.
* **Requests:** Web sitesine bağlanmak için.
* **CSV:** Verileri yapılandırılmış dosya formatında kaydetmek için.

## 🚀 Nasıl Çalışır?
1.  Bot, `books.toscrape.com` adresine gider.
2.  Belirlenen sayfa aralığını (Pagination) otomatik olarak gezer.
3.  Her kitaba ait **İsim, Fiyat** bilgisini bulur.
4.  Sonuçları `tum_kitaplar.csv` dosyasına kaydeder.

---
*Bu proje Yönetim Bilişim Sistemleri 3. Sınıf öğrencisi tarafından geliştirilmiştir.*