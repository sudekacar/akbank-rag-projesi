# Akbank Finansal Asistanı: RAG (Retrieval Augmented Generation) Uygulaması

Bu proje, Akbank GenAI Bootcamp kapsamında, RAG (Retrieval Augmented Generation) temelli bir chatbot geliştirerek, finansal dokümanlardan güvenilir bilgi çekme amacını taşımaktadır.

## 1. Projenin Amacı

Projenin temel amacı, Büyük Dil Modelleri'nin (LLM) en büyük sorunu olan "halüsinasyon" (uydurma cevaplar) eğilimini en aza indirmektir. LLM'i özel bir finansal bilgi havuzuna bağlayarak, yalnızca bu bağlamla ilgili, doğru ve kaynağı doğrulanabilir yanıtlar üretmek hedeflenmiştir.

## 2. Veri Seti Hakkında Bilgi

* **Tip:** Projeye özel olarak hazırlanmış finansal bilgi dokümanları (PDF/Metin).
* **İçerik:** Vadesiz mevduat hesapları, yatırım fonları, devlet tahvilleri, borçlanma araçları ve bireysel emeklilik sistemi gibi Akbank ve genel finansal terimleri içeren metinleri içerir.

## 3. Kullanılan Yöntemler ve Çözüm Mimarisi

Çözüm mimarisi, güçlü bir RAG zinciri üzerine kurulmuştur.

| Bileşen | Kullanılan Teknoloji | Amaç |
| :--- | :--- | :--- |
| **LLM (Büyük Dil Modeli)** | Google Gemini 2.5 Flash | Soru-Cevap üretimi ve yanıt sentezi. |
| **RAG Çerçevesi** | LangChain | Tüm RAG zincirinin (retrieval, prompt, model) yönetilmesi. |
| **Vektör Veritabanı** | ChromaDB | Doküman parçalarının vektör olarak saklanması ve hızlı aranması. |
| **Embedding Modeli** | SentenceTransformers (all-MiniLM-L6-v2) | Metinlerin yüksek boyutlu vektörlere dönüştürülmesi. |
| **Arayüzler** | Streamlit & Gradio | Kullanıcı dostu ve mobil uyumlu iki farklı web arayüzü sunulması. |

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

Projennin RAG sistemini test etmek için, finansal dokümanlarınızın içeriğine uygun, **farklı yetenekleri ölçen** aşağıdaki soruları kullanın:

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
