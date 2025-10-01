# Python **`pip*`** ile Paket Yönetimi

- `Pip`, Python için paket yükleme ve yönetim aracıdır. Python ile birlikte genellikle hazır olarak gelir ve kütüphaneleri, framework'leri ve diğer araçları kolayca normal sisteminize veya virtual environment üzerine kurmayı sağlar.

## 1. Temel Paket Kurulumu (Normal İndirme)

- Bir paketin en son sürümünü  PyPI (Python Package Index) üzerinden indirmek için kullanılır.
- **Bu komut ile indirme işlemleri yapılır:**
    ```bash 
    pip install {packet_name}
    ```
- Bu komutu ile istediğiniz paketleri indirebilirsiniz.
 
## 2. Belirli Bir Sürümü İndirme

- Bazenleri projenin uyumluluğu için eski sürümleri yüklemek gerekebilir.
- **Komut Yapısı:**
1.  **Tam olarak belirtilen sürüm:** ```==```
2.  **Minimum bu sürüm veya üstü:** ```>=``` (Paketin en az şu sürümü ve sonrası olsun, daha yenileri de olur)
3.  **Bu sürümden daha düşük:** ```<```
5.  **Uyumlu sürüm:** ```~=``` (Bu sürümle uyumlu en son sürümü kur, ama büyük ve riskli değişiklikler içeren ana sürümü atlama" anlamına gelir.)
- **Komut yapısını tam anlamak için örnekler:**

  - numpy kütüphanesinin tam olarak 1.23.5 sürümünü yüklemek için:
      ````bash
      pip install "numpy===1.23.5"
      ````
   - pandas kütüphanesinin 1.4.0 sürümünden daha yeni bir sürümünü yüklemek için:
    ```bash
   pip install "pandas>1.4.0"
    ```
- Çift tırnak içerisinde yazmanın sebebi bazı `bashlerde` sorun çıkartacağı için çift tırnak yazmak daha iyidir.

## 3. Dosyadan Paketleri Toplu Olarak Yükleme

- Projelerde kullanılan tüm paketleri ve sürümlerini bir metin dosyasına (genellikle `requirements.txt`) yazarak yönetmek yaygın bir yöntemdir. Bu, projenin başka bir bilgisayarda veya başka bir geliştirici tarafından kolayca kurulabilmesini sağlar.

- **Adım 1: `requirements.txt` Dosyasını Oluşturma**
- Bu dosya, her satırda bir paket olacak şekilde manuel olarak oluşturulabilir veya `pip freeze` komutu ile otomatik olarak oluşturulabilir **(Bkz. Madde 4).**
  - Örnek bir `requirements.txt` içeriği:
      ```text
        requests==2.28.1
        numpy>=1.20.0
        pandas
      ```
- **Adım 2: Dosyada ki paketleri yükleme:**
  - `-r` parametresi ile kolayca dosyanın içerisinde ki tüm paketler yüklenebilir.
      ```bash
      pip install -r requirements.txt 
      ```
- Bu komut, requirements.txt dosyasını okur ve içinde listelenen tüm paketleri belirtilen sürümleriyle birlikte kurar.

## 4. Yüklü Paketleri Listeleme **(`pip freeze`)**

- `pip freeze` komutu, mevcut Python ortamınızda yüklü olan tüm paketleri ve onların tam sürüm numaralarını `paket_adi==surum` formatında listeler.

  - **Komut:**
      ```bash
      pip freeze
      ```
  - **Çıktı Örneği:**
      ```text 
        certifi==2022.9.24
        charset-normalizer==2.1.1
        idna==3.4
        numpy==1.23.5
        requests==2.28.1
        urllib3==1.26.12
      ```
  - **`pip freeze` komutu ile `requirements.txt` oluşturma:**
      ```bash
      pip freeze > requirements.txt
      ```
- Bu komut, pip freeze komutunun çıktısını requirements.txt adında yeni bir dosyaya yönlendirir. Artık bu dosya, projenizi başkalarıyla paylaşmak veya farklı bir ortama taşımak için kullanılabilir.