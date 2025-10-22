import requests
from bs4 import BeautifulSoup
import os, re
import sys

# Dosyanın nerede oluşacağını belirleyen sabitler
OUTPUT_DIR = "data/financial_literacy"
OUTPUT_FILENAME = "tcmb_terimler.txt"
TCMB_URL = "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Egitim-Akademik/Terimler+Sozlugu"

try:
    print(f"🔗 TCMB URL'den veri çekiliyor: {TCMB_URL}")
    r = requests.get(TCMB_URL, timeout=15) # Zaman aşımı ekledik
    r.raise_for_status() # Hata kodu (4xx, 5xx) varsa exception fırlatır
    soup = BeautifulSoup(r.text, "html.parser")

    # Sayfadaki tüm metinleri al ve sadeleştir
    text = soup.get_text("\n", strip=True)
    
    # 3 veya daha fazla yeni satırı, 2 yeni satıra indirgeyerek metni temizle
    text = re.sub(r"\n{3,}", "\n\n", text) 
    
    # RAG için faydalı olacak şekilde gereksiz boşlukları temizle
    if len(text) < 100:
        raise ValueError("Çekilen metin çok kısa. Web sitesi yapısı değişmiş veya çekim başarısız.")
        
except requests.exceptions.RequestException as e:
    print(f"❌ Hata: Web sitesine bağlanılamadı veya istek zaman aşımına uğradı. İnternet bağlantınızı kontrol edin. Hata: {e}", file=sys.stderr)
    sys.exit(1)
except ValueError as e:
    print(f"❌ Hata: Veri çekimi başarılı değil. {e}", file=sys.stderr)
    sys.exit(1)


# ------------------
# DOSYAYA KAYIT KISMI
# ------------------
# Çıktı klasörünü oluştur (zaten varsa bir şey yapmaz)
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)

header = (
    "Source: " + TCMB_URL + "\n"
    "Category: financial_literacy\n"
    "Updated: 2025-10-20\n\n"
)

try:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header + text)

    print(f"✅ Başarılı! TCMB sözlüğü kaydedildi: {output_path}")

except IOError as e:
    print(f"❌ Hata: Dosyaya yazma izni yok veya dosya yolu geçersiz. Hata: {e}", file=sys.stderr)
    sys.exit(1)
