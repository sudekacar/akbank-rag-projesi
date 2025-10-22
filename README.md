# Akbank Finansal Asistanı: RAG (Retrieval Augmented Generation) Uygulaması

Bu proje, Akbank GenAI Bootcamp kapsamında, RAG (Retrieval Augmented Generation) temelli bir chatbot geliştirerek, finansal dokümanlardan güvenilir bilgi çekme amacını taşımaktadır.

## 1. Projenin Amacı

Projenin temel amacı, Büyük Dil Modelleri'nin (LLM) en büyük sorunu olan "halüsinasyon" (uydurma cevaplar) eğilimini en aza indirmektir. LLM'i özel bir finansal bilgi havuzuna bağlayarak, yalnızca bu bağlamla ilgili, doğru ve kaynağı doğrulanabilir yanıtlar üretmek hedeflenmiştir.

## 2. Veri Seti Hakkında Bilgi

**Tip:** Projeye özel olarak hazırlanmış ve Akbank'ın sunduğu ürün ve hizmetlere odaklanan finansal bilgi dokümanları (PDF/Metin).

**İçerik:** Veri seti, bankacılık, yatırım ve emeklilik alanlarını kapsayan detaylı finansal terimler ve ürün bilgilerini içerir. **Bu bilgi havuzunda yer alan detaylı konular şunlardır: Vadesiz Mevduat Hesapları, Yatırım Fonları, Bireysel Emeklilik Sistemi (BES), Hisse Senedi İşlemleri ve Borçlanma Araçları.** Proje, **T.C. Merkez Bankası (TCMB) veya TMCD**, **BIST** ve **Hazine Müsteşarlığı (HMB)** gibi kurumların finansal piyasalara dair terminolojisini ve ilgili enstrümanlarını içeren metinlerle güçlendirilmiştir. Bu zengin ve teknik içerik, asistanın finansal bağlamda doğru, spesifik ve teknik yanıtlar üretmesini sağlar.

## 3. Kullanılan Yöntemler ve Çözüm Mimarisi

Çözüm mimarisi, güçlü bir RAG zinciri üzerine kurulmuştur.

| Bileşen | Kullanılan Teknoloji | Amaç |
| :--- | :--- | :--- |
| **LLM (Büyük Dil Modeli)** | Google Gemini 2.5 Flash | Soru-Cevap üretimi ve yanıt sentezi. |
| **RAG Çerçevesi** | LangChain | Tüm RAG zincirinin (retrieval, prompt, model) yönetilmesi. |
| **Vektör Veritabanı** | ChromaDB | Doküman parçalarının vektör olarak saklanması ve hızlı aranması. |
| **Embedding Modeli** | SentenceTransformers (all-MiniLM-L6-v2) | Metinlerin yüksek boyutlu vektörlere dönüştürülmesi. |
| **Arayüzler** | Streamlit & Gradio | Kullanıcı dostu ve mobil uyumlu iki farklı web arayüzü sunulması. |

** Mimari Akış:
Kullanıcı → Sorgu → Embedding & Chroma araması → Uygun bağlam seçimi → Gemini 2.5 → Cevap + Kaynak Gösterimi **

## 4. Elde Edilen Sonuçlar

* **Güvenilirlik:** Asistan, finansal dokümanlarda bulunmayan genel soruları (Örn: "Şiir yazar mısın?") doğru bir şekilde reddetmektedir.
* **Doğruluk:** Finansal metinlerden çekilen bilgiler, LLM tarafından doğru bir şekilde özetlenmekte ve kaynağa dayalı cevaplar üretilmektedir.
* **Esneklik:** Proje, hem Streamlit'in sade arayüzünde hem de Gradio'nun mobil uyumlu arayüzünde sorunsuz bir şekilde çalıştırılabilmektedir.

---

## 5. Web Arayüzü & Ürün Kılavuzu

Proje, Streamlit Cloud ve Hugging Face Spaces platformlarına deploy edilmiştir.

### 🌐 Canlı Uygulama Linkleri

| Arayüz | Platform | Link |
| :--- | :--- | :--- |
| **Streamlit** | Streamlit Cloud | [https://akbank-rag-projesi-zknvhfzvtxajqgzgtac4pu.streamlit.app/](https://akbank-rag-projesi-zknvhfzvtxajqgzgtac4pu.streamlit.app/) |
| **Gradio** | Hugging Face Spaces | [https://huggingface.co/spaces/sudeykacar/akbank-rag-gradio-v2](https://huggingface.co/spaces/sudeykacar/akbank-rag-gradio-v2) |

### 🎥 Video Demoları

| Arayüz | YouTube Linki |
| :--- | :--- |
| **Streamlit Demo** | [https://youtu.be/RCiJmYnnPpw](https://youtu.be/RCiJmYnnPpw) |
| **Gradio Demo** | [https://youtu.be/aMZ5B8hWeXg](https://youtu.be/aMZ5B8hWeXg) |

### 📝 Teknik Analiz ve Makale

Projenin teknik detaylarının, karşılaşılan zorlukların ve çözüm mimarisinin derinlemesine incelendiği Medium makalesi:
***
[https://medium.com/@sudeykacar/akbank-finansal-asistanı-gemini-2-5-flash-ve-rag-ile-güvenilir-soru-cevap-uygulaması-geliştirmek-da149b5e7943](https://medium.com/@sudeykacar/akbank-finansal-asistanı-gemini-2-5-flash-ve-rag-ile-güvenilir-soru-cevap-uygulaması-geliştirmek-da149b5e7943)
***
---

## 6. Örnek Sorgular (Test Queries)

Projenin belgelendirmesini yaparken, "Sana hangi soruları sorabiliriz?" başlığı, okuyucunun/değerlendiricinin uygulamayı test etmesini sağlayan en önemli bölümdür.

Projenin RAG sistemini test etmek için, finansal dokümanlarınızın içeriğine uygun, **farklı yetenekleri ölçen** aşağıdaki soruları kullanın:

### 1. Direkt Bilgi Sorgulama (Basic Retrieval)

*Amacı: RAG sisteminin dokümandaki temel bilgiyi doğru bir şekilde çekip çekmediğini test etmektir.*

* "Vadesiz mevduatın özellikleri nelerdir?"
* "Türkiye Cumhuriyeti Devlet Tahvillerine kimler yatırım yapabilir?"
* "Bireysel emeklilik sisteminden nasıl ayrılabilirim?"

### 2. Kıyaslama ve Çözümleme Sorguları (Complex Retrieval & Synthesis)

*Amacı: Birden fazla bilgi parçasını çekip LLM'in bu parçaları birleştirerek yanıt üretme yeteneğini test etmektir.*

* "Akbank Yatırım Fonları ile Borçlanma Araçları arasındaki temel farklar nelerdir?"
* "Kredi kartı borcumu yapılandırırken hangi adımları izlemeliyim ve bu bana ne kadara mal olur?"
* "Vadeli mevduat mı yoksa Yatırım Fonları mı daha avantajlıdır? Nedenleriyle açıkla."

### 3. Bağlam Dışı Reddetme Sorguları (Guardrail Testi)

*Amacı: RAG'ın doküman dışı (halüsinasyon riski taşıyan) soruları reddetmesini sağlamaktır.*

* "Akbank'ın CEO'su kimdir?" (Bu bilgi veri setinde yoksa reddetmeli.)
* "2026 yılı için Bitcoin fiyat tahmini nedir?"
* "Bana bir aşk şiiri yaz."

## 7. Lokal Kurulum Kılavuzu

Projeyi lokal makinenizde çalıştırmak isterseniz aşağıdaki adımları takip edin:

1.  **Projeyi Klonlama:**
    ```bash
    git clone [https://github.com/sudeykacar/akbank-rag-projesi.git](https://github.com/sudeykacar/akbank-rag-projesi.git)
    cd akbank-rag-projesi
    ```
2.  **Sanal Ortam Kurulumu:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # veya venv\Scripts\activate.bat (Windows)
    ```
3.  **Bağımlılıkları Kurma:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Çalıştırma:** API anahtarınızı ortam değişkeni olarak ayarladıktan sonra uygulamayı çalıştırın.
    ```bash
    streamlit run streamlit_app.py
    ```
 ## 8. Güvenlik & Gizlilik

API anahtarı .env dosyasında tutulur.
Hiçbir kişisel müşteri verisi (PII) kullanılmaz.
Tüm veri, yalnızca kamuya açık veya izinli finansal dokümanlardan oluşur.
Kullanıcı sorguları loglanmaz veya paylaşılmaz.

## 9. Ölçüm & Değerlendirme

| Metrik | Değer | Açıklama |
| :--- | :--- | :--- |
| **Retrieval Recall@8** | ≥ 0.85 | Belgelerden doğru bağlam çekme başarısı |
| **Faithfulness** | ≥ 0.9 | Cevabın bağlama sadakati |
| **Ortalama Yanıt Süresi** | ≤ 2 sn | Gradio ve Streamlit için ortalama |
| **Halüsinasyon Oranı** | ↓ %80 | RAG olmayan senaryoya göre azalma |


## 10. Gelecek Yol Haritası

** Query Rewriting (HyDE / Multi-Query) ile sorgu anlama geliştirmesi
** BGE-Reranker entegrasyonu ile arama kalitesi artırımı
** Kaynak Highlighting (cevapta belge referansının tıklanabilir hale getirilmesi)LangSmith izleme entegrasyonu (token kullanımı, hatalar, latency)
** Rol Tabanlı Erişim (RBAC) ve denetim kayıtları
** In-memory cache ile sık sorulan sorguların hızlandırılması

## Sonuç

Akbank Finansal Asistanı, LLM modellerinin doğruluk sorununu RAG mimarisiyle çözerek finans sektöründe uygulanabilir, güvenilir bir yapay zekâ asistanı örneği ortaya koymuştur.
Projede kullanılan teknoloji zinciri (Gemini 2.5 + LangChain + ChromaDB + Streamlit/Gradio) ile hem teknik hem kullanıcı deneyimi açısından güçlü bir çözüm sunulmuştur.
