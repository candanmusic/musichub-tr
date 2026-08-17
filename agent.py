
import os, requests, datetime
from pathlib import Path

def main():
    print("MUSIC HUB TR v10.3 FINAL calisiyor")
    # mock haber
    title = f"{datetime.date.today()} - Gunluk Muzik Raporu"
    script = "Bugun Spotify Loud&Clear, YouTube Charts, TikTok Newsroom ve Suno blog verileri analiz edildi. Detaylar podcastte."
    Path("podcast/episodes").mkdir(parents=True, exist_ok=True)
    # RSS guncelle
    rss_path = Path("podcast/rss.xml")
    rss = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcasts-1.0.dtd">
<channel>
<title>CANDANMUSIC - Gunluk Muzik Raporu</title>
<link>https://candanmusic.github.io/musichub-tr/</link>
<description>Gunluk 5-10 dk</description>
<language>tr-tr</language>
<itunes:author>CANDANMUSIC</itunes:author>
<itunes:image href="https://candanmusic.github.io/musichub-tr/assets/candan_radyosu_gold.png"/>
<item>
<title>{title}</title>
<description>{script}</description>
<pubDate>{datetime.datetime.now()}</pubDate>
<enclosure url="https://candanmusic.github.io/musichub-tr/podcast/episodes/test.mp3" type="audio/mpeg"/>
</item>
</channel>
</rss>'''
    rss_path.write_text(rss, encoding="utf-8")
    print("RSS yazildi")

if __name__ == "__main__":
    main()
