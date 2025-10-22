# gradio_app.py

"""
Akbank Finans Asistanı Web Arayüzü (Gradio)

Bu dosya, Gradio kütüphanesi kullanarak hızlı bir model test arayüzü sağlar.
Tüm bilgi çekme (RAG) ve cevaplama mantığı 'rag_backend.py' dosyasında çalışır.

"""


import gradio as gr
from rag_backend import answer # Hata çözücü fonksiyonumuzu içeri aktarıyoruz

# Gradio arayüzünü tanımlama
iface = gr.Interface(
    fn=answer, 
    inputs=gr.Textbox(lines=5, label="Sorunuzu buraya yazın:"), 
    outputs="text",
    title="Akbank Finans Asistanı (Gemini + RAG)",
    description="Dosya içeriğine göre sorularınızı yanıtlar."
)

# Uygulamayı başlat
iface.launch()