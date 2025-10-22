# 🏦 Akbank Finansal Asistanı (Gemini + RAG)

Bu proje, Akbank GenAI Bootcamp kapsamında, Retrieval-Augmented Generation (RAG) mimarisini kullanarak finansal dokümanlardan bilgi çekmek ve kullanıcı sorularını güvenilir bir şekilde yanıtlamak amacıyla geliştirilmiştir. [cite_start]Amacımız, Büyük Dil Modelinin (LLM) uydurma (halüsinasyon) eğilimini, doğru ve bağlama dayalı bilgi sunarak ortadan kaldırmaktır[cite: 2].

## 1. Projenin Amacı

Projenin temel amacı, Akbank ve genel finansal terimler içeren özel bir veri seti üzerinde eğitilmiş, güvenilir bir Soru-Cevap (Question-Answering) sistemi oluşturmaktır. [cite_start]Kullanıcılar, web arayüzü üzerinden doğal dilde sorular sorabilir ve sistem, sadece sağlanan güncel finansal bağlama dayalı, doğru ve şeffaf cevaplar üretir[cite: 9].

## 2. Veri Seti Hakkında Bilgi

* **Veri Kaynağı:** Projede, çeşitli finansal terimler, ürün açıklamaları ve Akbank'a ait genel bilgileri içeren harici metin (.txt) dosyaları kullanılmıştır.
* **Parçalama (Chunking) Optimizasyonu:** LLM'in cevaba yetecek kadar bağlama sahip olması için, metin parçalama boyutu (`chunk_size`) **1600 karaktere** yükseltilmiştir. Bu teknik optimizasyon, RAG'ın "Bağlam Yetersizdir" gibi hatalarını azaltmıştır.
* [cite_start]**Not:** Veri setinin repoya eklenmesine gerek yoktur[cite: 13].

## [cite_start]3. Kullanılan Yöntemler ve Çözüm Mimariniz [cite: 11]

Proje, **LangChain** framework'ü üzerine kurulu **RAG** mimarisi kullanılarak geliştirilmiştir. [cite_start]Tüm teknik kararlar, Python dosyalarında yorum satırlarıyla detaylıca belgelenmiştir[cite: 7].

| Bileşen | Kullanılan Teknoloji | Teknik Gerekçe ve Karar (Özet) |
| :--- | :--- | :--- |
| **LLM (Generator)** | **Gemini 2.5 Flash** | Hızlı, yetenekli ve maliyet-etkin cevap üretimi için tercih edilmiştir. |
| **Embedding (Gömme)** | **`SentenceTransformerEmbeddings`** (`all-MiniLM-L6-v2`) | **KRİTİK DÜZELTME:** Gemini API'sinden kaynaklanan format/boyut hatalarını çözmek ve sistemi stabilize etmek için **yerel bir modele** geçilmiştir. |
| **Vektör Veritabanı** | **ChromaDB** | Yerel ve kolay entegrasyon sağlayan, kalıcı depolama çözümü olarak kullanılmıştır. |
| **RAG Çekim Miktarı (Retriever)** | **k = 10** | RAG'ın doğru bilgiyi kaçırma riskini azaltmak için, varsayılan 4 parça yerine en benzer **10 bağlam parçasının** LLM'e sunulması sağlanmıştır. |
| **Arayüzler** | **Streamlit & Gradio** | Hızlı prototipleme ve test kolaylığı için iki farklı web arayüzü sunulmuştur. |

## [cite_start]4. Elde Edilen Sonuçlar ve Mühendislik Düzeltmeleri [cite: 12]

* **Stabilite Başarısı:** Streamlit/Gradio arayüzleriyle yaşanan `RuntimeError: Event loop is closed` hatası, `rag_backend.py` dosyasında **asenkron (async) çağrıdan senkron (invoke) çağrıya** geçilerek çözülmüş ve stabil çalışma garanti edilmiştir.
* **Guardrail (İstem Koruması):** Prompt mühendisliği ile LLM'in uydurması engellenmiştir. Veri setinde bulunmayan bilgiler sorulduğunda, LLM uydurmak yerine, açıkça **"Bağlam yetersizdir"** şeklinde şeffaf bir uyarı vermektedir.
* **Doğru Bilgi Erişimi:** Yapılan RAG optimizasyonları (Embedding modeli değişikliği, k=10, chunk boyutu), sistemin karşılaştırmalı ve detaylı finansal sorulara **yüksek güvenilirlikte** cevaplar üretmesini sağlamıştır.

---

### [cite_start]🌐 Web Uygulaması ve Deploy Linki [cite: 13]

Projenin canlı web arayüzüne (Streamlit Cloud) aşağıdaki adresten ulaşabilirsiniz:

**WEB UYGULAMASI LİNKİ:**
`[LÜTFEN BURAYA STREAMLIT CLOUD'DAN ALDIĞINIZ CANLI URL'Yİ YAPIŞTIRIN]`
