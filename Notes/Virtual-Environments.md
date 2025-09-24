# Virtual Environments Notlarım

## Sanal Ortamlar Neden Gerekli? Manuel Yönetimin Çilesi

Diyelim ki iki farklı proje üzerinde çalışıyorum:

1.  **Eski Proje (Legacy API Entegrasyonu):**
    * Dosya Yolu: `C:\Users\Kullanici\Documents\Projeler\Eski_CRM_API`
    * Bu proje, `requests` kütüphanesinin eski ve spesifik bir versiyonu olan `2.18.0` ile çalışmak **zorunda.** Çünkü entegre olduğu sistem sadece bu versiyonla uyumlu.

2.  **Yeni Proje (Modern Web Scraper):**
    * Dosya Yolu: `C:\Users\Kullanici\Documents\Projeler\Yeni_Veri_Kaziyici`
    * Bu projede ise `requests` kütüphanesinin getirdiği yeni özelliklerden faydalanmak için en güncel versiyonu olan `2.31.0`'ı kullanmam gerekiyor.

Eğer sanal ortam kullanmazsam, bu iki kütüphane de bilgisayarımın ana Python kurulumu içine (`site-packages` klasörüne) kurulur. Bu durumda ne olur?

* `pip install requests==2.18.0` komutunu çalıştırdığımda, eski proje için gereken versiyon kurulur.
* Sonra yeni projeye geçip `pip install requests==2.31.0` dediğimde, `pip` eski versiyonu **silip** yerine yenisini kurar.
* Bu sefer de eski projeyi çalıştırmak istediğimde, yeni versiyonla uyumsuz olduğu için proje çöker.

Bu döngüden çıkmak için kütüphaneleri sürekli manuel olarak silip yeniden kurmam gerekir. Bu hem aşırı yorucu hem de hata yapmaya çok açık bir yöntem. Her proje geçişinde doğru kütüphane versiyonlarını hatırlamak ve yönetmek tam bir baş ağrısı.

## Çözüm: Sanal Ortamlar (Virtual Environments)

İşte bu noktada sanal ortamlar devreye giriyor ve hayat kurtarıyor.

-   **Sanal ortam, temel olarak belirli bir python projesini çalıştırmak için kullandığımız ek kütüphanelerle birlikte python'un bir kopyasıdır.**

Yani her proje için Python'un ve kütüphanelerin izole, bağımsız bir kopyasını oluşturuyoruz. Böylece `Eski_CRM_API` projesinin sanal ortamında `requests==2.18.0` varken, `Yeni_Veri_Kaziyici` projesinin tamamen ayrı sanal ortamında `requests==2.31.0` olabilir. Bunlar birbirine asla karışmaz.

### Araçlar ve İşleyiş

Neyse ki bu **sıkıcı işi bizim için yapacak araçlar var.‘*’**

-   `pipenv`
-   `virtualenv`
-   Python'un standart kütüphanesinde de bir tane var:
    -   `venv` (En yaygın ve tavsiye edilen*)

---
Kısacası, bir projeye başlarken o projeye özel bir sanal ortam oluşturup aktive ediyorum. Sonrasında `pip` ile kurduğum her şey sadece o projenin izole ortamına kuruluyor. Global Python kurulumum temiz ve projelerim birbiriyle çakışmadan, kararlı bir şekilde çalışıyor. İşte bu yüzden sanal ortamlar Python geliştirmede bir lüks değil, bir **zorunluluktur**.