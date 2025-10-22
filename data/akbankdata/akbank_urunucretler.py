# fetch_akbank_ucretler_menu.py
import os, re, requests
from bs4 import BeautifulSoup

PRIMARY = "https://www.akbank.com/urun-ve-hizmet-ucretleri"
ALT     = "https://www.akbank.com/faiz-ve-oranlar/Sayfalar/urun-ve-hizmet-ucretleri.aspx"
CDX_API = "https://web.archive.org/cdx/search/cdx"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8",
}

def fetch(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=25)
        if r.status_code == 200 and len(r.text) > 1000:
            return r.text
    except requests.RequestException:
        pass
    return None

def find_wayback_snapshot(url, year_from="2022"):
    params = {
        "url": url,
        "output": "json",
        "fl": "timestamp,original,statuscode",
        "filter": "statuscode:200",
        "limit": "1",
        "from": year_from,
    }
    try:
        r = requests.get(CDX_API, params=params, timeout=25)
        if r.ok:
            data = r.json()
            if len(data) > 1:
                ts = data[1][0]
                return f"https://web.archive.org/web/{ts}/{url}"
    except requests.RequestException:
        pass
    return None

def html_to_clean_text(html):
    soup = BeautifulSoup(html, "html.parser")
    for sel in ["script","style","nav","header","footer"]:
        for t in soup.select(sel): t.decompose()
    txt = soup.get_text("\n", strip=True)
    # tipik gürültüyü azalt
    noise = [
        r"Akbank\.com.*", r"Arama Yap.*", r"Bizi Takip Edin.*",
        r"Her Hakkı Akbank.*", r"Çerez .* Politikası.*",
        r"Merhaba, ben Akbank Asistan!.*", r"EN\b", r"Ana Sayfa",
        r"Akbanklı Ol", r"Blog", r"İletişim", r"KVKK.*",
    ]
    for pat in noise:
        txt = re.sub(pat, "", txt, flags=re.IGNORECASE)
    txt = re.sub(r"\n{3,}", "\n\n", txt).strip()
    return txt

def main():
    os.makedirs("data/bank_products", exist_ok=True)
    target = None

    # 1) Ana URL
    html = fetch(PRIMARY)
    if html:
        target = PRIMARY
    else:
        # 2) Alternatif URL
        html = fetch(ALT)
        if html:
            target = ALT
        else:
            # 3) Wayback arşiv kopyası
            snap = find_wayback_snapshot(PRIMARY) or find_wayback_snapshot(ALT)
            if not snap:
                raise SystemExit("× İçerik alınamadı (canlı ve arşiv başarısız).")
            html = fetch(snap)
            if not html:
                raise SystemExit("× Wayback snapshot indirilemedi.")
            target = snap

    text = html_to_clean_text(html)
    header = (
        "Source: " + target + "\n"
        "Category: bank_products\n"
        "Note: Menü/başlık ağırlıklı içerik; ayrıntı/rakamlar alt sayfalardadır.\n\n"
    )
    out = "data/bank_products/akbank_ucretler_index.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(header + text + "\n")
    print("✅ Kaydedildi →", out)

if __name__ == "__main__":
    main()
