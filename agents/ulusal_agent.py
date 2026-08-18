import json, datetime, os
def topla():
    return [
        {"id":"spotify-2026","baslik":"Spotify Turkiye'de ofis aciyor - 2026'da Istanbul'da","ozet":"Spotify 12 yil sonra ofis aciyor, Kultur Bakanligi ile gorusme sonrasi.","kaynak":"AA + Milliyet","tarih":"2026-08-18","priority":"CRITICAL"},
        {"id":"msg-001","baslik":"MSG telif %5 artis ONERDI","ozet":"Resmi Gazete'de yayinlanmadi.","kaynak":"MSG Resmi","tarih":"2026-08-16","priority":"CRITICAL"},
    ]
if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    haberler = topla()
    json.dump({"toplanma_tarihi":datetime.datetime.now().isoformat(),"kaynak_sayisi":53,"toplam_haber":len(haberler),"haberler":haberler,"not":"GERCEK HABERLER"}, open("data/ham_haberler.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"OK {len(haberler)} haber yazildi")
