# UiPath REFramework: Gemini AI Destekli POD Tasarım Otomasyonu

Bu proje, Print-on-Demand (POD) e-ticaret süreçleri için geliştirilmiş, manuel tasarım yükünü ortadan kaldıran ve süreçleri SEO uyumlu, baskıya hazır (300 DPI) hale getiren uçtan uca bir RPA çözümüdür.

## 💡 Sesli Demo Videosu
Projenin otonom çalışma prensibini, Gemini AI & Python entegrasyonlarını ve REFramework mimarisini anlattığım 3.5 dakikalık inceleme videosunu aşağıdan izleyebilirsiniz.
*(Video Linki veya Görseli Buraya Gelecek)*

## 🎯 Projenin Amacı ve İş Değeri (Business Value)
Öğretmen nişi başta olmak üzere, e-ticaret mağazaları için tasarım üretim ve optimizasyon süreçleri otomatize edilmiştir. Bu robot sayesinde:
* Manuel tasarım isimlendirme ve kalite kontrol süreçlerinde harcanan zaman %90 oranında azaltılmıştır.
* Orijinal kalite kaybı yaşanmadan, sıfır hatalı ve arama motoru (SEO) algoritmalarına tam uyumlu ürünler elde edilmektedir.

## 🛠️ Kullanılan Teknolojiler
* **UiPath Studio:** Süreç orkestrasyonu (REFramework)
* **Google Gemini AI:** Görüntü analizi ve SEO uyumlu isimlendirme
* **Python (rembg, Pillow):** Arka plan temizleme ve 300 DPI çözünürlük optimizasyonu
* **UiPath Orchestrator:** Kuyruk (Queue) ve Asset yönetimi

## 🏗️ Sistem Mimarisi ve Akış (Workflow)
Proje, kurumsal UiPath standartlarına uygun olarak **Dispatcher** ve **Performer** olmak üzere iki ayrı süreçten oluşur:
1. **Dispatcher:** Şablon verilerini okur ve işlenecek öğeleri güvenli bir şekilde Orchestrator Queue'ya (Kuyruk) aktarır.
2. **Performer (REFramework):** Kuyruktaki her bir öğeyi (Transaction Item) sırayla alır, yapay zeka ile görselini üretir, Python ile optimize eder ve sonucu raporlar.

*(Buraya projenin nasıl çalıştığını gösteren bir Akış Şeması / Flowchart görseli eklenecek)*

## ✉️ Akıllı Hata Yönetimi (SE & BRE) ve Raporlama
REFramework standartlarına uygun olarak hatalar iki farklı kategoride ele alınır ve Gemini AI yardımıyla kullanıcı dostu bir dille raporlanır:
* **System Exception (SE):** Web sitesinin çökmesi veya internet kopması gibi sistemsel hatalarda robot işlemi durdurup güvenli kapanış (Close All Applications) yapar ve IT ekibine mail atar.
* **Business Rule Exception (BRE):** Üretilen görselin baskı standartlarına uymaması gibi iş kuralı ihlallerinde robot durmaz; hatalı öğeyi atlayıp (Skip) bir sonraki tasarımdan çalışmaya devam eder.

## 🚀 Kurulum ve Çalıştırma
1. Projeyi bilgisayarınıza klonlayın: `git clone <repo-url>`
2. Python bağımlılıklarını yükleyin: `pip install rembg Pillow`
3. UiPath Orchestrator üzerinde `Config_Assets` ve `Design_Queue` tanımlamalarını yapın.
4. `Config.xlsx` dosyasındaki lokal klasör yollarını güncelleyip `Main.xaml` üzerinden süreci başlatın.

## ✨ Gelecek Planları (Roadmap)
* Tasarım oranını bozmadan şeffaf kenar payı (padding) ekleyerek farklı tuval ölçülerine uyarlama.
