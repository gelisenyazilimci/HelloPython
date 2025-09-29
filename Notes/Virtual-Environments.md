# Virtual Environments Notlarım

## Adım 0: Projenin Python Sürümüne Karar Vermek

Sanal ortam oluşturmaya başlamadan önceki en kritik adım, proje için hangi Python sürümünü kullanacağıma karar vermek. Çünkü sanal ortam, benim bilgisayarımda zaten kurulu olan bir Python sürümünün (`python 3.9`, `python 3.10` vb.) bir kopyası olarak oluşturulur.

**Neden bu kadar önemli?**
- **Uyumluluk:** Kullanacağım kütüphaneler belirli Python versiyonlarını gerektirebilir. Projenin başında yanlış sürüm seçmek, ileride kütüphane uyumsuzluklarına yol açar.
- **Dağıtım (Deployment):** Projeyi sunucuya yüklediğimde, sunucudaki Python sürümü ile geliştirme ortamımdaki sürümün aynı olması beklenmedik hataları önler.

Bu yüzden, projeye başlamadan "Bu proje Python 3.10 ile geliştirilecek" kararını verip, sanal ortamı o sürümü kullanarak oluşturmak en temiz başlangıçtır.

## Sanal Ortamlar Neden Gerekli? Manuel Yönetimin Çilesi

Diyelim ki iki farklı proje üzerinde aynı anda çalışıyorum:

1.  **Eski Proje (Legacy Sistem):**
    * Dosya Yolu: `C:\Projeler\Eski_CRM_API`
    * Bu proje, `requests` kütüphanesinin eski ve spesifik bir versiyonu olan `2.18.0` ile çalışmak **zorunda.**

2.  **Yeni Proje (Modern API):**
    * Dosya Yolu: `C:\Projeler\Yeni_Veri_Kaziyici`
    * Bu projede ise `requests` kütüphanesinin en güncel versiyonu olan `2.31.0`'ı kullanmam gerekiyor.

Eğer sanal ortam kullanmazsam, bu iki kütüphane de bilgisayarımın tek ve ana Python kurulumuna yazılır. Bir projeden diğerine geçtiğimde, `pip install --upgrade requests` veya `pip install requests==2.18.0` komutlarıyla sürekli kütüphane versiyonunu **manuel olarak değiştirmek zorunda kalırım.** Bu hem aşırı yorucu hem de hata yapmaya çok açık bir yöntemdir. Bir versiyonu güncellemeyi unuttuğumda projelerimden biri kesinlikle çöker.

## Çözüm: İzole ve Temiz Proje Ortamları

İşte bu kaosu önlemek için sanal ortamlar var.

-   **Sanal ortam, temel olarak belirli bir python projesini çalıştırmak için kullandığımız ek kütüphanelerle birlikte python'un bir kopyasıdır.**

Her proje kendi izole Python "kum havuzuna" sahip olur. `Eski_CRM_API` projesinin sanal ortamında `requests==2.18.0` varken, `Yeni_Veri_Kaziyici` projesinin ortamında `requests==2.31.0` olabilir. Birbirlerine asla dokunmazlar.

### Hayatı Kolaylaştıran Araçlar

Neyse ki, bu **sıkıcı işi bizim için yapacak araçlar var:**
-   `virtualenv`
-   `pipenv`
-   Python'un standart kütüphanesinde gelen:
    -   **`venv`** (Genellikle ilk tercih)

## Pratik kullanım (**`venv`** komutu ile + sadece Windows için not alıyorum*)
### 1. Sanal Ortamı Oluşturma

- Terminali açıp projenin klosörünün içerisine gidip, ardından o klasörünün içinde `venv` adında bir sanal ortam oluşturmak için şu komutu çalıştırmamız yeterli:
```bash
  # python3 -m venv <sanal_ortam_adi>
  # Genellikle sanal ortam adı olarak "venv" kullanılır!
  # Ornek olarak şu komutu girdiğimizi varsayalım: "python3 -m venv venv"
  # Veya en son sürüm sanal ortam kurmayacaksanız: "python3 -3.x -m venv {folder_name}" bunu yazmanız yeterli  
```
- Bu yukarıda yazdığım örnek komut  proje klasörümün içinde venv adında bir alt klasör oluşturacak. Bu klasör, Python'un bir kopyasını ve kütüphaneleri barındırır.

### 2. Sanal Ortamı Aktif Etme

- Oluşturmak yeterli olmayacak, terminalin bu ortamı kullanabilmesi bu ortamı aktif etmem gerekli.
 ```bash 
    .\venv\Scripts\activate
 ```

- Aktivasyon başarılı olduğunda, komut satırının başında (venv) gibi bir ifade belirir. Bu, artık çalıştıracağım python ve pip komutlarının bu sanal ortama ait olduğunu gösterir.

- Bu komut ile aktif ettin zaten ve içerisindesin artık. `python --version` yazdığın zaman atadığın version geliyor. 
- `Örnek: (venv) C:\Projeler\Yeni_Veri_Kaziyici>`

### 3. Sanal Ortamı Kapatma 
- İş bittiğinde veya başka bir projeye geçmek istediğim zaman, ortamdan çıkmak için tek yapmam gereken terminale şunu yazmak:
 ```bash 
    deactivate
 ```

- Komut satırının başındaki (venv) ifadesi kaybolacaktır.