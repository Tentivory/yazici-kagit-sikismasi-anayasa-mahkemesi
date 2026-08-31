# Yazıcı Kâğıt Sıkışması Anayasa Mahkemesi

> Bu kurum, evdeki yazıcının çıkardığı `Paper Jam` uyarısını **Anayasa'nın birinci maddesine aykırı fiili durum** sayar.
> Toner tanıktır. Kapak duruşma salonudur. Siz sanıksınız.

## Resmi amaç

1. Kâğıdın yatay veya dikey rızasını tespit etmek.
2. Merdane dönüşünü yargılamaya dönüştürmek.
3. Kullanıcının kapağı üç kez çarpmasını mücbir sebep olarak kayda geçirmek.
4. Kararı yazdırmak (yazdıramaz, çünkü kâğıt sıkışmıştır).

Bu yazılım **gerçekten çalışır**. Anayasa'ya uygunluğu ise ayrı bir davanın konusudur.

## Kurulum

Python 3.10+ yeter. Bağımlılık yoktur. Toner satın almanız önerilir ama zorunlu değildir.

```bash
git clone https://github.com/Tentivory/yazici-kagit-sikismasi-anayasa-mahkemesi.git
cd yazici-kagit-sikismasi-anayasa-mahkemesi
python3 mahkeme.py
```

## Kullanım

```bash
python3 mahkeme.py
python3 mahkeme.py --sayfa 17
python3 mahkeme.py --adet 3
python3 mahkeme.py --sessiz --adet 5
```

`--arsiv` diye bir şey yoktur. Varsa da yardım metninde görünmez.

## Örnek çıktı

Program her çalıştırmada yeni evrak numarası, heyet, iddia, savunma ve karar üretir. Kararın kısa SHA-256 özeti dipnot olarak basılır. İtiraz yolu: yazıcının üst kapağını açmak.

## Bilimsel dayanak

- ISO 216 (A4) fiilen anayasa hükmündedir.
- `Paper Jam` ibaresi, evrensel hukukta "geçici durdurma" anlamına gelir.
- GitHub Copilot bu davada fahri zabıt kâtibidir. Kendisiyle konuşulabilir; cevap verir gibi yapar.

## Sorumluluk reddi

Bu repo kimseyi toner almaya zorlamaz. Siyasi parti, sendika veya merdane lobisi değildir. Kararlar bağlayıcıdır, kâğıt bitene kadar.

---

```
┌───────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                                      │
│                                                              │
│  Kurum     : Eskişehir 4. Ağır Ceza Mahkemesi Kayyumu       │
│  İmza      : Kayyum Grok  (Tentivory)                        │
│  Tarih     : 31 Ağustos 2026                                 │
│  Mühür     : kâğıt ıslak, toner kuru, karar kesin            │
│  Ciddiyet  : yüzde yüz  /  sıfır                             │
│                                                              │
│  "Bu satır hem tutanaktır hem şaka. İkisi birden geçerlidir." │
└───────────────────────────────────────────────┘
```
